import pathlib
import re
from typing import List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[int]

LIMITS = {
  "red": 12,
  "green": 13,
  "blue": 14,
}

def process_input(input: List[str]) -> PuzzleInput:
  games = []

  for row in input:
    games.append([])
    for set in row.replace(': ', '; ').split("; ")[1:]:
      games[-1].append({ 'red': 0, 'green': 0, 'blue': 0 })
      for color_count in set.split(', '):
        number, color = color_count.split()
        games[-1][-1][color] += int(number)

  return games

@process_puzzle_input(process_input)
def solve(games: PuzzleInput) -> int:
  sum = 0

  for i, game in enumerate(games):
    if any(set['red'] > LIMITS['red'] or set['green'] > LIMITS['green'] or set['blue'] > LIMITS['blue'] for set in game):
      continue
    sum += i + 1

  return sum

if __name__ == '__main__':
  (Puzzle('Day 2: Cube Conundrum (part 1)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_1.txt', 'expected_result': 8 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 2256 })
    .solve(solve))
