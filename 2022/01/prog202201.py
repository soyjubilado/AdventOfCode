#!/usr/bin/python3
#file created 2022-Nov-30 20:38
"""https://adventofcode.com/2022/day/1"""

DATA = 'data202201.txt'
#DATA = 'testdata202201.txt'


def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def main():
  lines = GetData(DATA)
  current = 0
  all_elves = []
  for i in lines:
    if i:
      current += int(i)
    else:
      all_elves.append(current)
      current = 0

  print(f'maximum seen was {max(all_elves)}')
  print(f'top three {sum(list(reversed(sorted(all_elves)))[:3])}')


if __name__ == '__main__':
  main()
