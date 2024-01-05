from itertools import product
import pathlib
from typing import List, Optional

from advent_helper.colors import END, RED
from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[List[str]]

def process_input(input: List[str]) -> PuzzleInput:
  return [[*row] for row in input]

@process_puzzle_input(process_input)
def solve(engine_schematic: PuzzleInput) -> int:
  schematic = Schematic(engine_schematic)
  number = 0

  for y in range(schematic.size[1]):
    for x in range(schematic.size[0]):
      schematic.set_coordinate(x, y)

      if schematic.is_on_symbol():
        for prod in product((-1, 0, 1), repeat=2):
          schematic.set_coordinate(x + prod[0], y + prod[1])
          if schematic.is_on_digit():
            number += schematic.find_number()

  return number

class Schematic:
  def __init__(self, schematic: List[str]):
    self._schematic = schematic
    self._coordinate = (0, 0)
    self.size = (len(schematic[0]), len(schematic))

  def current_char(self) -> str:
    return self._schematic[self._coordinate[1]][self._coordinate[0]]

  def set_current_char(self, char: str) -> 'Schematic':
    self._schematic[self._coordinate[1]][self._coordinate[0]] = char

    return self

  def is_on_symbol(self) -> bool:
    return self.current_char() != '.' and not self.current_char().isalnum()

  def is_on_digit(self) -> bool:
    return self.current_char().isdigit()

  def set_coordinate(self, x: int, y: int) -> Optional['Schematic']:
    if x < 0 or y < 0 or x >= self.size[0] or y >= self.size[1]:
      return None

    self._coordinate = (x, y)

    return self

  def find_number(self) -> Optional[int]:
    if not self.is_on_digit():
      return None

    original_coordinate = self._coordinate

    number = self.current_char()
    self.set_current_char('.')

    if self.set_coordinate(self._coordinate[0] - 1, self._coordinate[1]):
      while self.is_on_digit():
        number = self.current_char() + number
        self.set_current_char('.')
        if not self.set_coordinate(self._coordinate[0] - 1, self._coordinate[1]):
          break

    self.set_coordinate(original_coordinate[0], original_coordinate[1])

    if self.set_coordinate(self._coordinate[0] + 1, self._coordinate[1]):
      while self.is_on_digit():
        number = number + self.current_char()
        self.set_current_char('.')
        if not self.set_coordinate(self._coordinate[0] + 1, self._coordinate[1]):
          break

    self.set_coordinate(original_coordinate[0], original_coordinate[1])

    return int(number)

  def print(self) -> None:
    print('------------------ schematic ------------------')
    for y in range(self.size[1]):
      for x in range(self.size[0]):
        char = self._schematic[y][x]
        if x == self._coordinate[0] and y == self._coordinate[1]:
          print(f'{RED}{char}{END}', end='')
        else:
          print(char, end='')
      print()

if __name__ == '__main__':
  (Puzzle('Day 3: Gear Ratios (part 1)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_1.txt', 'expected_result': 4361 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 535078 })
    .solve(solve))
