#!/usr/bin/python3
#file created 2021-Dec-13 20:54
"""https://adventofcode.com/2021/day/14

Part 1 and Part 2 now use the same code. Originally, I coded part 1 naively
to get a quick answer, doing the simulation the way the reaction was described
in the problem. Growth was exponential, doubling with each additional round.
Ten rounds finished in under a second. Fifteen took about a second, and
doubled each consecutive round. Additionally, if the polymer were stored in an
array of bytes, it would have required a terrabyte of ram to hold it.

The more efficient approach for part 2:

  * Translate the original polymer into a dictionary of 2-element items,
    with a count of how many there are of that pair.
    'ABAB' -> {'AB': 2, 'BA':1}
  * Every round, create a new dictionary from the old dictionary and the
    generation rules. For example, if you start with 'AB' and the rule AB -> C
    you get {'AC': 1, 'CB': 1}
  * After the final round, count up your elements. Every element is counted
    twice in the dictionary except the first and last ones of the original
    polymer, which never change.
"""

from collections import defaultdict

ROUNDS = 40
DATA = 'data202114.txt'
# DATA = 'testdata202114.txt'


def GetData(datafile):
  """Parse data"""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def PolymerDict(polymer):
  """Turn the original polymer into a dictionary of pairs."""
  polymer_dict = defaultdict(lambda: 0)
  for i in range(len(polymer) - 1):
    polymer_dict[polymer[i:i+2]] += 1
  return polymer_dict


def ReactPolymerDict(polymer_dict, rules):
  """Given a polymer_dict and rules, create the next polymer_dict."""
  new_polymer_dict = defaultdict(lambda: 0)
  for reactant, amount in polymer_dict.items():
    a, c = reactant
    b = rules[reactant]
    new_polymer_dict[a + b] += amount
    new_polymer_dict[b + c] += amount
  return new_polymer_dict


def CountPolymerDict(polymer_dict, start_char, end_char):
  """Given a polymer represented by a dictionary of all its pairs, count
     the number of elements and subtract the most from the least."""
  element_frequency = defaultdict(lambda: 0)
  for pair, count in polymer_dict.items():
    a, b = pair
    element_frequency[a] += count
    element_frequency[b] += count

  # End characters are only counted once. This brings everyone up to twice.
  element_frequency[start_char] += 1
  element_frequency[end_char] += 1

  frequencies = element_frequency.values()
  return (max(frequencies) - min(frequencies))//2


def main():
  lines = GetData(DATA)
  polymer = lines[0]
  print(f'Starting polymer: {polymer}')
  rules = {}
  for l in lines[2:]:
    pair, element = l.split(' -> ')
    rules[pair] = element

  polymer_dict = PolymerDict(polymer)
  for r in range(ROUNDS):
    polymer_dict = ReactPolymerDict(polymer_dict, rules)
    answer = CountPolymerDict(polymer_dict, polymer[0], polymer[-1])
    print(f'Part 2, round {r+1}: {answer}')


if __name__ == '__main__':
  main()
