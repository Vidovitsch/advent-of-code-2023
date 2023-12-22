import pathlib
import re
from typing import List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[int]

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

  for game in games:

    max_red = 0
    max_green = 0
    max_blue = 0

    for set in game:
      if set['red'] > max_red:
        max_red = set['red']
      if set['green'] > max_green:
        max_green = set['green']
      if set['blue'] > max_blue:
        max_blue = set['blue']

    sum += max_red * max_green * max_blue

  return sum

if __name__ == '__main__':
  (Puzzle('Day 2: Cube Conundrum (part 2)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_2.txt', 'expected_result': 2286 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 74229 })
    .solve(solve))
