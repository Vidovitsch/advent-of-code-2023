import pathlib
from typing import List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[List[int]]

def process_input(input: List[str]) -> PuzzleInput:
  return [list(map(int, row.split())) for row in input]

@process_puzzle_input(process_input)
def solve(report: PuzzleInput) -> int:
  return sum(find_extrapolation(line) for line in report)

def find_extrapolation(sequence: List[int]) -> int:
  if all(num == 0 for num in sequence):
    return 0

  next_sequence = [num2 - num1 for num1, num2 in zip(sequence, sequence[1:])]
  return sequence[0] - find_extrapolation(next_sequence)

if __name__ == '__main__':
  (Puzzle('Day 9: Mirage Maintenance (part 2)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_1.txt', 'expected_result': 2 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 1068 })
    .solve(solve))
