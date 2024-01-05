from collections import Counter
import math
import pathlib
from typing import List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[List[str]]

def process_input(input: List[str]) -> PuzzleInput:
  processed_input = []

  for row in input:
    for numbers in row.split(': ')[1:]:
      winning, own = numbers.split(' | ')
      processed_input.append(
        [
          [number for number in winning.split(' ') if number.isdigit()],
          [number for number in own.split(' ') if number.isdigit()]
        ]
      )

  return processed_input

@process_puzzle_input(process_input)
def solve(scratchcards: PuzzleInput) -> int:
  total = 0

  for card_nr, card in enumerate(scratchcards):
    counter = Counter(card[0] + card[1])
    total += math.floor(2 ** (sum(counter.values()) - len(counter.keys()) - 1))

  return total

if __name__ == '__main__':
  (Puzzle('Day 4: Scratchcards (part 1)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_1.txt', 'expected_result': 13 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 25571 })
    .solve(solve))
