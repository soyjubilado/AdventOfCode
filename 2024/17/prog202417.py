#!/usr/bin/python3
# file created 2024-Dec-17 17:01
"""https://adventofcode.com/2024/day/17"""

DATA = 'data202417.txt'
# DATA = 'testdata202417.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetComputer(lines):
  """Create a computer and program from input."""
  reg_a = int(lines[0].split(':')[1].strip())
  reg_b = int(lines[1].split(':')[1].strip())
  reg_c = int(lines[2].split(':')[1].strip())
  prog_str = lines[4].split(':')[1].strip().split(',')
  prog = [int(i) for i in prog_str]
  return Computer(reg_a, reg_b, reg_c), prog


class Computer():
  """Class to represent the 3-bit computer."""

  def __init__(self, a, b, c, instr_pointer=0):
    """Initialize the registers."""
    self.a = a
    self.b = b
    self.c = c
    self.instr = instr_pointer
    self.output = []

  def __repr__(self):
    return (f'Computer: a={self.a} b={self.b} c={self.c} instr={self.instr} '
            f'out={self.output}')

  def Combo(self, operand):
    """Return value of a combo operand."""
    return {0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: self.a,
            5: self.b,
            6: self.c}[operand]

  def Run(self, opcode, operand):
    """Run one opcode."""
    def ADV(x):
      self.a = int(self.a / (2**self.Combo(x)))

    def BXL(x):
      self.b = self.b ^ x

    def BST(x):
      self.b = self.Combo(x) % 8

    def JNZ(x):
      self.instr = self.instr + 2 if not self.a else x

    def BXC(_):
      self.b = self.b ^ self.c

    def OUT(x):
      self.output.append(self.Combo(x) % 8)

    def BDV(x):
      self.b = int(self.a / (2**self.Combo(x)))

    def CDV(x):
      self.c = int(self.a / (2**self.Combo(x)))

    op = {0: ADV,
          1: BXL,
          2: BST,
          3: JNZ,
          4: BXC,
          5: OUT,
          6: BDV,
          7: CDV
         }

    op[opcode](operand)

    if opcode != 3:
      self.instr += 2

    return self.instr

  def RunProg(self, prog):
    """Run the entire program."""
    while self.instr < len(prog):
      op, operand = prog[self.instr:self.instr + 2]
      self.Run(op, operand)

    return self.output


def Part1(lines):
  """Part 1."""
  c, prog = GetComputer(lines)
  output = c.RunProg(prog)
  return ','.join([str(i) for i in output])


def Part2(_):
  """Part 2."""
  return None


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  # print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
