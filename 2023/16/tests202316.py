#!/usr/bin/env python3
"""unit tests for progYYYYDD.py"""

import sys
sys.path.insert(0, '../lib/')
from h_test import h_test

from prog202316 import *
from grid import *



def test_next_cell():
  DATA = 'testdata202316.txt'
  lines = GetData(DATA)
  grid = GridWrap(lines)
  beam = Beam(grid, (0,0), EAST)
  print(f'{beam.current} -> {beam.next_cell()}')



def main():
  """main"""
  test_move()
  


if __name__ == '__main__':
  main()
