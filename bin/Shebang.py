#!/usr/bin/env python3
"""Create a skeleton file that includes the code for reading the data file."""

import os
import stat
import sys
from textwrap import dedent
import time

YEAR = '2024'

def WriteFile(daynum, year):
  filename = f'prog{year}{daynum:>02}.py'
  if os.path.exists(filename):
    print(f'{filename} already exists.\n\n  rm {filename}\n\n')
    sys.exit()
  with open(filename, 'w') as fh:
    fh.write('#!/usr/bin/python3\n')
    fh.write(f'# file created {time.strftime("%Y-%b-%d %H:%M")}\n')
    fh.write(f'"""https://adventofcode.com/{year}/day/{daynum}"""\n\n')
    fh.write(f"DATA = 'data{year}{daynum:>02}.txt'\n")
    fh.write(f"#DATA = 'testdata{year}{daynum:>02}.txt'\n\n")
    fh.write(dedent('''
                    def GetData(datafile):
                      """Read input into a list of lines."""
                      lines = []
                      with open(datafile, 'r') as fh:
                        lines = [i.strip() for i in fh]
                      return lines


                    def Part1(lines):
                      """Part 1."""
                      return None


                    def Part2(lines):
                      """Part 2."""
                      return None


                    def main():
                      """main"""
                      lines = GetData(DATA)
                      print(f'Part 1: {Part1(lines)}')
                      print(f'Part 2: {Part2(lines)}')


                    if __name__ == '__main__':
                      main()
                    '''))
  os.chmod(filename, stat.S_IRWXU)


def main(argv):
  if len(argv) < 2:
    print('Need an argument.')
    sys.exit()
  year = YEAR if len(argv) < 3 else argv[2]
  WriteFile(argv[1], year)


main(sys.argv)
