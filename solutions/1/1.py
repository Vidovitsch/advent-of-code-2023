import pathlib
from typing import List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[int]

def process_input(input: List[str]) -> PuzzleInput:
  return input

@process_puzzle_input(process_input)
def solve(input: PuzzleInput) -> int:
  return 0

if __name__ == '__main__':
  (Puzzle('Day 1: Trebuchet?! (part 1)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test.txt', 'expected_result': 142 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': "?" })
    .solve(solve))