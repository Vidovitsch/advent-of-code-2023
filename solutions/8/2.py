import pathlib
from typing import Any, Dict, List, Tuple
import math
import itertools

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = Tuple[str, Dict[str, Tuple[str, str]]]

def process_input(input: List[str]) -> PuzzleInput:
  network = {}

  for node in input[1:]:
    key, value = node.split(' = ')
    value = value.lstrip('(')
    value = value.rstrip(')')
    value = tuple(value.split(', '))

    network[key] = value

  return (input[0], network)

@process_puzzle_input(process_input)
def solve(map: PuzzleInput) -> int:
  steps = [find_end_node_steps(node, map) for node in map[1].keys() if node[-1] == 'A']
  return math.lcm(*list(itertools.chain(*steps)))

def find_end_node_steps(start_node: str, map: PuzzleInput) -> List[Tuple[int, int]]:
  instructions = map[0]
  network = map[1]

  end_node_steps = {}

  step_count = 0
  instruction_index = 0
  current_node = start_node

  while f'{instruction_index}-{current_node}' not in end_node_steps:
    if current_node[-1] == 'Z':
      end_node_steps[f'{instruction_index}-{current_node}'] = step_count

    if instructions[instruction_index] == 'R':
      current_node = network[current_node][1]
    else:
      current_node = network[current_node][0]

    if instruction_index == len(instructions) - 1:
      instruction_index = 0
    else:
      instruction_index += 1
    step_count += 1

  return list(end_node_steps.values())

if __name__ == '__main__':
  (Puzzle('Day 8: Haunted Wasteland (part 2)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_3.txt', 'expected_result': 6 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 10668805667831 })
    .solve(solve))
