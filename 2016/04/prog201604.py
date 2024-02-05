#!/usr/bin/python3
# file created 2023-Jan-17 16:53
"""https://adventofcode.com/2016/day/4"""

from collections import defaultdict


DATA = 'data201604.txt'
# DATA = 'testdata201604.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def NameIdChecksum(line):
  """Split the line into constituent parts."""
  name_parts, checksum_part = line.split('[')
  checksum = checksum_part.replace(']', '')
  name_parts = name_parts.split('-')
  name = name_parts[:-1]
  id_str = name_parts[-1]
  return name, int(id_str), checksum


def ValidChecksum(name, chksum):
  """True if the room name is valid according to the checksum."""
  frequency_map = defaultdict(lambda: 0)
  for n in name:
    for l in n:
      frequency_map[l] += 1
  letter_tuples = sorted(list(frequency_map.items()),
                         key=lambda x: (-x[1], x[0]))
  expected_chksum = ''.join([k for k, f in letter_tuples[:5]])
  return chksum == expected_chksum


def RotN(letter, n):
  """Rotate a lowercase letter n spaces through the alphabet."""
  assert 'a' <= letter <= 'z'
  n_of_alpha = ord(letter) - ord('a')
  new_n = (n_of_alpha + n) % 26
  new_letter = chr(new_n + ord('a'))
  return new_letter


def DecryptedRoomName(name, id_num):
  """Given a room name and id_number, return the decrypted string."""
  output = []
  for n in name:
    decrypted = ''.join([RotN(l, id_num) for l in n])
    output.append(decrypted)
  output.append(str(id_num))
  return ' '.join(output)


def Part1(lines):
  """Part 1"""
  valid_names = []
  total = 0
  for line in lines:
    name, id_num, chksum = NameIdChecksum(line)
    if ValidChecksum(name, chksum):
      valid_names.append((name, id_num, chksum))
      total += id_num
  return total, valid_names


def Part2(valid_names):
  """Part 2"""
  for name, id_num, _ in valid_names:
    decrypted = DecryptedRoomName(name, id_num)
    if decrypted.startswith('north'):
      print(decrypted)


def main():
  """main"""
  lines = GetData(DATA)
  pt_1_answer, valid_names = Part1(lines)
  print(f'Part 1: {pt_1_answer}')
  print(f'Part 2:', end=' ')
  Part2(valid_names)


if __name__ == '__main__':
  main()
