#!/usr/bin/python3
#file created 2022-Dec-10 22:16
"""https://adventofcode.com/2022/day/11"""

from collections import deque, defaultdict

DATA = 'data202211.txt'
DATA = 'testdata202211.txt'
BIGNUM = 13 * 3 * 7 * 2 * 19 * 5 * 11 * 17
SMALLNUM = 23 * 19 * 13 * 17

def DataMonkeys():
  m = []
  m.append(Monkey([89, 73, 66, 57, 64, 80],
                  lambda x: x * 3, lambda x: 6 if not x % 13 else 2))
  m.append(Monkey([83, 78, 81, 55, 81, 59, 69],
                  lambda x: x + 1, lambda x: 7 if not x % 3 else 4))
  m.append(Monkey([76, 91, 58, 85],
                  lambda x: x * 13, lambda x: 1 if not x % 7 else 4))
  m.append(Monkey([71, 72, 74, 76, 68],
                  lambda x: x * x, lambda x: 6 if not x % 2 else 0))
  m.append(Monkey([98, 85, 84],
                  lambda x: x + 7, lambda x: 5 if not x % 19 else 7))
  m.append(Monkey([78],
                  lambda x: x + 8, lambda x: 3 if not x % 5 else 0))
  m.append(Monkey([86, 70, 60, 88, 88, 78, 74, 83],
                  lambda x: x + 4, lambda x: 1 if not x % 11 else 2))
  m.append(Monkey([81, 58],
                  lambda x: x + 5, lambda x: 3 if not x % 17 else 5))
  return m


def TestMonkeys():
  m = []
  m.append(Monkey([79, 98],
                   lambda x: x * 19, lambda x: 2 if not x % 23 else 3))
  m.append(Monkey([54, 65, 75, 74],
                   lambda x: x + 6, lambda x: 2 if not x % 19 else 0))
  m.append(Monkey([79, 60, 97],
              lambda x: x * x, lambda x: 1 if not x % 13 else 3))
  m.append(Monkey([74], lambda x: x + 3, lambda x: 0 if not x % 17 else 1))
  return m


def Nop(*args, **kwargs):
  pass

def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


class Monkey(object):
  def __init__(self, starting, operation, test):
    self.starting = deque(starting)
    self.operation = operation
    self.test = test
    self.inspected = len(self.starting)

  def SetInspectation(self):
    self.inspected = len(self.starting)

  def Catch(self, item):
    self.starting.append(item)

def RunRound(monkeys, inspect_dict, print=Nop):
  for idx, m in enumerate(monkeys):
    print(f'Monkey {idx}:')
    inspect_dict[idx] += len(m.starting)
    for _ in range(len(m.starting)):
      item = m.starting.popleft() 
      print(f'  Monkey inspects item level {item}')
      item = m.operation(item)
      # print(f'    new worry level is {item}')
      # item //= 3
      # print(f'    dividing by 3 gives {item}')
      item %= BIGNUM
      # item %= SMALLNUM
      destination = m.test(item)
      print(f'    item {item} is thrown to monkey {destination}')
      monkeys[destination].Catch(item)
  return monkeys

def main():
  """main"""
  lines = GetData(DATA)
  # print(lines)
  """
  """
  # m = DataMonkeys()
  m = DataMonkeys()
  monkey_map = defaultdict(lambda: 0) 
  for round in range(10000):
    print(f'Round {round}')
    """
    for idx in range(len(m)):
      print(f'Monkey {idx}: {m[idx].starting}')
      print(f'   adding {len(m[idx].starting)}')
    """
    m = RunRound(m, monkey_map)
  top_scores = list(reversed(sorted(monkey_map.values())))
  print(monkey_map)
  print(top_scores)
  print({top_scores[0] * top_scores[1]})


if __name__ == '__main__':
  main()
