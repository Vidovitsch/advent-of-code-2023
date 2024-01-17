from collections import Counter
import pathlib
from typing import List
from itertools import chain

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

  for i in range(len(almanac['seeds']))[::2]:
    seed_range = (almanac['seeds'][i], almanac['seeds'][i + 1])

    soil_ranges = get_destination_ranges(almanac['seed-to-soil'], [seed_range])
    fertilizer_ranges = get_destination_ranges(almanac['soil-to-fertilizer'], soil_ranges)
    water_ranges = get_destination_ranges(almanac['fertilizer-to-water'], fertilizer_ranges)
    light_ranges = get_destination_ranges(almanac['water-to-light'], water_ranges)
    temperature_ranges = get_destination_ranges(almanac['light-to-temperature'], light_ranges)
    humidity_ranges = get_destination_ranges(almanac['temperature-to-humidity'], temperature_ranges)
    locations += get_destination_ranges(almanac['humidity-to-location'], humidity_ranges)

  return sorted(locations)[0][0]

def get_destination_ranges(almanac_ranges, source_ranges):
  destination_ranges = []

  for source_range in source_ranges:
    done_ranges = []
    for almanac_range in almanac_ranges:
        almanac_range_start = almanac_range[1]
        almanac_range_length = almanac_range[2]

        max_start = max(almanac_range_start, source_range[0])
        min_end = min(almanac_range_start + almanac_range_length, source_range[0] + source_range[1])

        if min_end <= max_start:
          continue
        else:
          done_ranges.append((max_start, min_end))
          destination_ranges.append((max_start - almanac_range_start + almanac_range[0], min_end - max_start))

    gaps = range_gaps(source_range[0], source_range[0] + source_range[1], done_ranges)
    destination_ranges += [(g[0], g[1] - g[0]) for g in gaps]

  return destination_ranges

def range_gaps(a, b, ranges):
    ranges = sorted(ranges)
    flat = chain((a-1,), chain.from_iterable(ranges), (b+1,))
    return [(x+1, y-1) for x, y in zip(flat, flat) if x+1 < y]

if __name__ == '__main__':
  (Puzzle('Day 5: If You Give A Seed A Fertilizer (part 2)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_1.txt', 'expected_result': 46 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 12634632 })
    .solve(solve))
