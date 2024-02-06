#!/usr/bin/python3
# file created 2024-Jan-23 08:47
"""https://adventofcode.com/2023/day/12"""

from functools import lru_cache
from itertools import combinations


DATA = 'data202312.txt'
# DATA = 'testdata202312.txt'


def get_data(datafile):
  """Read input into a list of lines."""
  spring_records = []
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  for line in lines:
    spring, record_str = line.split()
    record = [int(i) for i in record_str.split(',')]
    spring_records.append((spring, record))
  return spring_records


def all_combos(my_list):
  """returns all combos of all sizes of elements of my_list"""
  combos = [combinations(my_list, i) for i in range(0, len(my_list)+1)]
  for c in combos:
    for n in c:
      yield n


def spring_conditions(spring_str):
  """Given a spring, return its conditions as a list of ints."""
  retval = []
  subs = spring_str.split('.')
  for s in subs:
    hashes = s.count('#')
    if hashes:
      retval.append(hashes)
  return retval


def candidates(subspring, record):
  """Given a subspring and a record, return all the possible
     subsprings, and the remainder.
     example: ('????#?', 3) ->

              ('XXX?#?', '#?') ok
              ('?XXX#?', '')   no
              ('??XXX?', '')   ok
              ('???XXX', '')   ok
  """
  candidates_remainders = []
  width = record
  for i in range(len(subspring) - width + 1):
    spring_copy = list(subspring)
    for j in range(i, i + width):
      spring_copy[j] = 'X'
    if i + width + 1 < len(subspring) and spring_copy[i + width] != '#':
      remainder = ''.join(spring_copy[i + width + 1:])
    else:
      remainder = ''
    candidates_remainders.append((''.join(spring_copy), remainder))
  return candidates_remainders


def candidate_is_valid(candidate_remainder):
  """Given a single candidate and remainder, return whether the combo
     is valid"""
  candidate, remainder = candidate_remainder
  return candidate.count('#') == remainder.count('#')


def split_spring(spring):
  """Split a spring so that no subspring contains '.'"""
  broken_spring = spring.split('.')
  return [i for i in broken_spring if i]


@lru_cache(maxsize=None)
def count_viable(sub_springs, record, depth=0):
  """Given a list of sub_springs (str list) and record (int list), return
     the number of variants that match record.
  """
  if not record:
    if not sub_springs:
      return 1
    if all(['#' not in s for s in sub_springs]):
      return 1
    if ['#' in s for s in sub_springs]:
      return 0
  if record:
    if not sub_springs:
      return 0
  all_count = 0
  subspring = sub_springs[0]
  variants = [c for c in candidates(subspring, record[0])
              if candidate_is_valid(c)]

  for _, remainder in variants:
    if remainder != '':
      next_subspring = [remainder]
      next_subspring.extend(sub_springs[1:])
    else:
      next_subspring = sub_springs[1:]
    next_record = record[1:]
    sub_count = count_viable(tuple(next_subspring), tuple(next_record),
                             depth=depth+1)
    all_count += sub_count
  if not '#' in subspring:
    # '????' can be replaced by '....' legitimately
    all_count += count_viable(tuple(sub_springs[1:]), tuple(record[:]))

  return all_count


def count_matches(spring_rec):
  """A less than brute force method. This function is the entry point
     for the recursive count_viable() function."""
  spring, record = spring_rec
  sub_springs = tuple(split_spring(spring))
  return count_viable(sub_springs, tuple(record))


def part_1(spring_records):
  """Part 1"""
  matches_sum = 0
  for spring_rec in spring_records:
    matches = count_matches(spring_rec)
    matches_sum += matches
  return matches_sum


def make_fat(spring_records):
  """Quintuple the records for part 2."""
  answers = []
  for spring, record in spring_records:
    new_spring = '?'.join([spring for _ in range(5)])
    new_record = record * 5
    answers.append((new_spring, new_record))
  return answers


def part_2(spring_records):
  """part 2"""
  fat_spring_records = make_fat(spring_records)
  matches_sum = 0
  for spring_rec in fat_spring_records:
    matches = count_matches(spring_rec)
    matches_sum += matches
  return matches_sum


def main():
  """main"""
  spring_records = get_data(DATA)
  print(f'Part 1: {part_1(spring_records)}')
  print(f'Part 2: {part_2(spring_records)}')


if __name__ == '__main__':
  main()
