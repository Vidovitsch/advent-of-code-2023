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
          [
            [number for number in winning.split(' ') if number.isdigit()],
            [number for number in own.split(' ') if number.isdigit()]
          ]
        ]
      )

  return processed_input

@process_puzzle_input(process_input)
def solve(scratchcards: PuzzleInput) -> int:
  for i in range(len(scratchcards)):
    for card in scratchcards[i]:
      counter = Counter(card[0] + card[1])
      for j in range(sum(counter.values()) - len(counter.keys())):
        scratchcards[i + j + 1].append(scratchcards[i + j + 1][0])

  return sum(len(cards) for cards in scratchcards)

if __name__ == '__main__':
  (Puzzle('Day 4: Scratchcards (part 2)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_1.txt', 'expected_result': 30 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 8805731 })
    .solve(solve))
