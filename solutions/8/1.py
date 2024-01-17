import pathlib
from typing import Any, List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[Any]

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
  instructions = map[0]
  network = map[1]

  current_node = 'AAA'
  step_count = 0
  while current_node != 'ZZZ':
    instruction = instructions[step_count % len(instructions)]

    if instruction == 'R':
      current_node = network[current_node][1]
    else:
      current_node = network[current_node][0]

    step_count += 1

  return step_count

if __name__ == '__main__':
  (Puzzle('Day 8: Haunted Wasteland (part 1)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_1.txt', 'expected_result': 2 })
    .add_test({ 'input_path': CURRENT / 'test_2.txt', 'expected_result': 6 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 16697 })
    .solve(solve))
