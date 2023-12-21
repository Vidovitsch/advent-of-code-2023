import pathlib
import re
from typing import List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[int]

STRING_TO_DIGIT = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9"
}

def process_input(input: List[str]) -> PuzzleInput:
  return input

@process_puzzle_input(process_input)
def solve(input: PuzzleInput) -> int:
  sum = 0
  for line in input:
    numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    sum += int(STRING_TO_DIGIT.get(numbers[0], numbers[0]) + STRING_TO_DIGIT.get(numbers[-1], numbers[-1]))

  return sum

if __name__ == '__main__':
  (Puzzle('Day 1: Trebuchet?! (part 2)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_2.txt', 'expected_result': 281 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 55218 })
    .solve(solve))
