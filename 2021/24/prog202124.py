#!/usr/bin/python3
#file created 2022-Jan-13 20:48
"""https://adventofcode.com/2021/day/24"""

from collections import deque

DATA = 'data202124.txt'
# DATA = 'testdata202124.txt'


def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


class ALU(object):
  def __init__(self, input_queue):
    assert isinstance(input_queue, deque)
    self.input = input_queue
    self.register = {'w': 0,
                     'x': 0,
                     'y': 0,
                     'z': 0}

  def inp(self, a):
    self.register[a] = self.input.popleft()

  def add(self, a, b):
    self.register[a] += b

  def mul(self, a, b):
    self.register[a] *= b

  def div(self, a, b):
    self.register[a] //= b

  def mod(self, a, b):
    self.register[a] %= b

  def eql(self, a, b):
    self.register[a] = 1 if self.register[a] == b else 0

  def execute(self, instr, args):
    if instr == 'inp':
      self.inp(args[0])
      return
    if args[1] in ['w', 'x', 'y', 'z']:
      arg1 = self.register[args[1]]
    else:
      arg1 = int(args[1])
    arg0 = args[0]
    # print(f' -> {instr} {arg0} {arg1}')

    if instr == 'add':
      self.add(arg0, arg1)
    elif instr == 'mul':
      self.mul(arg0, arg1)
    elif instr == 'div':
      self.div(arg0, arg1)
    elif instr == 'mod':
      self.mod(arg0, arg1)
    elif instr == 'eql':
      self.eql(arg0, arg1)
    else:
      raise Exception

  def __str__(self):
    retval = ''
    registers = [f'{self.register[i]:>3}' for i in ['w', 'x', 'y', 'z']]
    retval += '|'.join(registers)
    return retval


def Digits():
  x = 0
  while True:
    x = x%9 + 1
    yield 10 - x



def main(argv):
  lines = GetData(DATA)
  input_q = deque([10, 2])
  #                1  2  3  4  5  6  7  8  9  0  1  2  3  4
  # input_q = deque([9, 9, 5, 9, 8, 9, 6, 3, 9, 9, 9, 9, 7, 1])
  input_q = deque([9, 3, 1, 5, 1, 4, 1, 1, 7, 1, 1, 2, 1, 1])
  if len(argv) > 1:
    input_q[0] = int(sys.argv[1])
  alu = ALU(input_q)
  print(alu)
  for line in lines:
    print(f'{line:<9}', end=' -- ', flush=True)
    tokens = line.split()
    instr = tokens[0]
    args = tokens[1:]
    alu.execute(instr, args)
    print(alu)


if __name__ == '__main__':
  import sys
  main(sys.argv)
  # 99598963999971
  # 0 if w[4] == w[3]+4
  # 0 if w[7] == w[6]-3
  # 0 if w[9] == w[8]+6
  # 0 if w[11] == w[10]
  # 0 if w[12] == w[5]+1
  # 0 if w[13] == w[2]-2
  # 0 if w[14] == w[1]-8
  # smallest 93151411711211
