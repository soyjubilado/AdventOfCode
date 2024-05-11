#!/usr/bin/python3
#file created 2021-Dec-15 20:21
"""https://adventofcode.com/2021/day/16

The interesting part for me was turning the bit string into a python iterator,
and creating the Chomp method to consume exactly how many bits I wanted to bite
off. Then it was just a matter of recursively building the parse tree.
"""

DATA = 'data202116.txt'
# DATA = 'testdata202116.txt'

HEX2BIN = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
           '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
           'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110',
           'F': '1111'}


def GetData(datafile):
  """Parse input."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Hex2Binary(line):
  """Given a hexadecimal string, convert to a binary string."""
  binary_str = ''
  for i in line:
    binary_str += HEX2BIN[i]
  return binary_str


class Packet(object):
  """Packet class."""

  def __init__(self, version, packet_type, value=None):
    self.version = version
    self.type = packet_type
    self.value = value
    self.sub_packets = []

  def Value(self):
    """Populate self.value and return that value."""
    if self.type == 4:
      pass
    elif self.type == 0:
      self.value = sum([i.Value() for i in self.sub_packets])
    elif self.type == 1:
      self.value = 1
      for p in self.sub_packets:
        self.value *= p.Value()
    elif self.type == 2:
      self.value = min([i.Value() for i in self.sub_packets])
    elif self.type == 3:
      self.value = max([i.Value() for i in self.sub_packets])
    elif self.type == 5:
      s1 = self.sub_packets[0].Value()
      s2 = self.sub_packets[1].Value()
      self.value = 1 if s1 > s2 else 0
    elif self.type == 6:
      s1 = self.sub_packets[0].Value()
      s2 = self.sub_packets[1].Value()
      self.value = 1 if s1 < s2 else 0
    elif self.type == 7:
      s1 = self.sub_packets[0].Value()
      s2 = self.sub_packets[1].Value()
      self.value = 1 if s1 == s2 else 0
    else:
      raise Exception
    return self.value

  def Print(self, depth=0):
    """Print this packet, indenting sub packets by depth."""
    indent = '.' * depth
    print(f'{indent}version: {self.version} '
          f'type: {self.type} value: {self.value}')
    for p in self.sub_packets:
      p.Print(depth=depth + 1)

  def SumOfVersions(self):
    """For part 1, prints sum of all the packet versions."""
    total = self.version
    for s in self.sub_packets:
      total += s.SumOfVersions()
    return total


def Chomp(my_bits, how_many, as_string=False):
  """Chomps off n bits and returns a decimal number string of bits."""
  retval = ''
  for _ in range(how_many):
    retval += next(my_bits)
  if not as_string:
    retval = int(retval, 2)
  return retval


def ParsePacket(bits):
  """Given an iterable string of bits, return a Packet object."""
  version = Chomp(bits, 3)
  p_type = Chomp(bits, 3)
  if p_type == 4: # literal
    last = False
    value = ''
    while not last:
      last = Chomp(bits, 1) == 0
      value += Chomp(bits, 4, as_string=True)
    p = Packet(version, p_type, int(value, 2))

  else:
    length_type = Chomp(bits, 1)
    p = Packet(version, p_type)
    sub_pack_objs = []
    if length_type == 0:
      sub_pack_len = Chomp(bits, 15)
      sub_pack_bits = Chomp(bits, sub_pack_len, as_string=True)
      sub_bits = iter(sub_pack_bits)
      while True:
        try:
          sub_pack_objs.append(ParsePacket(sub_bits))
        except StopIteration:
          break

    elif length_type == 1:
      num_sub_packs = Chomp(bits, 11)
      for _ in range(num_sub_packs):
        sub_pack_objs.append(ParsePacket(bits))
    p.sub_packets = sub_pack_objs
  return p


def main():
  """Main function."""
  line = GetData(DATA)[0]
  bits = iter(Hex2Binary(line))
  top_packet = ParsePacket(bits)
  top_packet.Value() # this populates self.value so Print() is more meaningful.
  top_packet.Print()
  print(f'\nPart 1, sum of versions: {top_packet.SumOfVersions()}')
  print(f'Part 2, sum of values: {top_packet.Value()}')


if __name__ == '__main__':
  main()
