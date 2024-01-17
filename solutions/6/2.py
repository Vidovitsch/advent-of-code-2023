import pathlib
import re
from typing import List, Tuple

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = Tuple[int, int]

def process_input(input: List[str]) -> PuzzleInput:
  return (int(''.join(re.findall(r'\d+', input[0]))), int(''.join(re.findall(r'\d+', input[1]))))

@process_puzzle_input(process_input)
def solve(race: PuzzleInput) -> int:
  return get_winning_options_count(race)

def get_winning_options_count(race: Tuple[int, int]) -> int:
  winning_options_count = 0

  for hold_time in range(race[0] + 1):
    travel_distance = (race[0] - hold_time) * hold_time
    if travel_distance > race[1]:
      winning_options_count += 1

  return winning_options_count

if __name__ == '__main__':
  (Puzzle('Day 6: Wait For It (part 2)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_1.txt', 'expected_result': 71503 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 42515755 })
    .solve(solve))
