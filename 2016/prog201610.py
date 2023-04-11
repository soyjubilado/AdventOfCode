#!/usr/bin/python3
# file created 2023-Apr-10 21:19
"""https://adventofcode.com/2016/day/10

Create a dictionary of bots. Each bot contains a pointer to the dictionary
that it's in, and also a dictionary of outputs. Every round, iterate through
the bot dictionary and every bot runs the PitchValues() method. This method
will check to see whether the bot is holding two values; if it is, it pitches
them to the designated destinations. Keep doing this until there are no more
changes (about 26 rounds for my input).
"""

DATA = 'data201610.txt'
#DATA = 'testdata201610.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


class Bot():
  """A bot class"""

  def __init__(self, name, low, high, bot_dict, outputs):
    self.name = name
    self.low_dest = low
    self.high_dest = high
    self.bot_dict = bot_dict
    self.values = []
    self.outputs = outputs

  def PitchValues(self):
    """Check whether bot is holding 2 values; and if it is, pitch the high
       and low values to destinations self.low_dest and self.high_dest
    """
    if len(self.values) < 2:
      return None, None
    low, high = sorted(self.values)

    if self.low_dest[0] == 'bot':
      self.bot_dict[self.low_dest[1]].Catches(low)
    else:
      self.outputs[self.low_dest[1]] = low

    if self.high_dest[0] == 'bot':
      self.bot_dict[self.high_dest[1]].Catches(high)
    else:
      self.outputs[self.high_dest[1]] = high

    self.values = []
    return low, high

  def Catches(self, num):
    """Given a number, add it to one's own list of values"""
    self.values.append(int(num))


def FillBotDict(lines):
  """Parse data and populate dictionaries.
    values{} contains the initial values and what bots get them
    bots{} is a dictionary of bots keyed on the bot number
    outputs{} is an initally empty dictionary that holds output data
    every bot contains a pointer to bots and outputs
  """
  values = {}
  bots = {}
  outputs = {}
  for line in lines:
    line = line.split()
    if line[0] == 'value':
      val, destination_bot = int(line[1]), line[-1]
      values[val] = destination_bot
    elif line[0] == 'bot':
      bot_name, low_dest, high_dest = line[1], line[5:7], line[10:12]
      bots[bot_name] = Bot(bot_name, low_dest, high_dest, bots, outputs)
    else:
      raise Exception

  return values, bots, outputs


def main():
  """main"""
  Part1_Condition = (17, 61)
  lines = GetData(DATA)
  values, bots, outputs = FillBotDict(lines)
  for value, bot in values.items():
    bots[bot].Catches(value)

  # bots keep pitching chips until there are no more swaps
  changes = 1
  while changes:
    changes = 0
    for bot in bots.values():
      low, high = bot.PitchValues()
      changes += 1 if low is not None else 0
      if (low, high) == Part1_Condition:
        part_1_answer = bot.name

  part_2_answer = 1
  for i in ['0', '1', '2']:
    part_2_answer *= outputs[i]
  print(f'Part 1: {part_1_answer}')
  print(f'Part 2: {part_2_answer}')


if __name__ == '__main__':
  main()
