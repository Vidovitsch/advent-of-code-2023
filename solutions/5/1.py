from collections import Counter
import pathlib
from typing import List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[List[str]]

def process_input(input: List[str]) -> PuzzleInput:
  almanac = {
    'seeds': list(map(int, input[0].split(': ')[1].split())),
  }

  map_name = None
  for line in input[1:]:
    if not line.split()[0].isdigit():
      map_name = line.split(' map')[0]
      almanac[map_name] = []
    else:
      almanac[map_name].append(list(map(int, line.split())))

  return almanac

@process_puzzle_input(process_input)
def solve(almanac: PuzzleInput) -> int:
  locations = []

  for seed in almanac['seeds']:
    soil = get_destination(almanac['seed-to-soil'], seed)
    fertilizer = get_destination(almanac['soil-to-fertilizer'], soil)
    water = get_destination(almanac['fertilizer-to-water'], fertilizer)
    light = get_destination(almanac['water-to-light'], water)
    temperature = get_destination(almanac['light-to-temperature'], light)
    humidity = get_destination(almanac['temperature-to-humidity'], temperature)
    locations.append(get_destination(almanac['humidity-to-location'], humidity))

  return min(locations)

def get_destination(ranges, source) -> int:
  for r in ranges:
    if r[1] <= source <= r[1] + r[2]:
      return source - r[1] + r[0]

  return source


if __name__ == '__main__':
  (Puzzle('Day 5: If You Give A Seed A Fertilizer (part 1)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_1.txt', 'expected_result': 35 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 51752125 })
    .solve(solve))
