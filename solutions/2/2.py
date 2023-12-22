import pathlib
import re
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
  (Puzzle('Day 2: Cube Conundrum (part 2)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_2.txt', 'expected_result': 281 })
    .solve(solve))
