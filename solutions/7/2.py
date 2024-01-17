import pathlib
from typing import Any, List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

class Hand():
  CARD_STRENGTHS = {
    'J': 1,
    '1': 2,
    '2': 3,
    '3': 4,
    '4': 5,
    '5': 6,
    '6': 7,
    '7': 8,
    '8': 9,
    '9': 10,
    'T': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
  }

  def __init__(self, hand: str, bid: int) -> 'Hand':
    self.hand = hand
    self.bid = bid

  @classmethod
  def from_input_line(cls, input_line: str) -> 'Hand':
    hand, bid = input_line.split()
    return Hand(hand, int(bid))

  @property
  def type(self) -> int:
    card_counts = {}
    for card in self.hand:
      card_counts.setdefault(card, 0)
      card_counts[card] += 1

    counts = list(card_counts.values())

    if 5 in counts:
      return 7
    if 4 in counts:
      if 'J' in card_counts:
        return 7
      else:
        return 6
    if 3 in counts and 2 in counts:
      if 'J' in card_counts:
        return 7
      else:
        return 5
    if 3 in counts:
      if 'J' in card_counts:
        return 6
      else:
        return 4
    if counts.count(2) == 2:
      if 'J' in card_counts:
        if card_counts['J'] == 2:
          return 6
        else:
          return 5
      else:
        return 3
    if 2 in counts:
       if 'J' in card_counts:
         return 4
       else:
        return 2

    if 'J' in card_counts:
      return 2
    else:
      return 1

  def __gt__(self, other):
    if self.type > other.type:
      return True
    elif self.type < other.type:
      return False
    else:
      for current_card, other_card in zip(self.hand, other.hand):
        if self.CARD_STRENGTHS[current_card] > self.CARD_STRENGTHS[other_card]:
          return True
        if self.CARD_STRENGTHS[current_card] < self.CARD_STRENGTHS[other_card]:
          return False
      return False

PuzzleInput = List[Hand]

def process_input(input: List[str]) -> PuzzleInput:
  return [Hand.from_input_line(line) for line in input]

@process_puzzle_input(process_input)
def solve(hands: PuzzleInput) -> int:
  total_winnings = 0

  for i, hand in enumerate(sorted(hands)):
    total_winnings += hand.bid * (i + 1)

  return total_winnings

if __name__ == '__main__':
  (Puzzle('Day 7: Camel Cards (part 2)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_1.txt', 'expected_result': 5905 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 251824095 })
    .solve(solve))
