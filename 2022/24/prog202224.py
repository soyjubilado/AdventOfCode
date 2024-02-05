#!/usr/bin/python3
# file created 2022-Dec-24 09:51
"""https://adventofcode.com/2022/day/24

Longer and probably slower than it needs to be. Create a blizzard class, and
a dictionary holding all the locations of blizzards. Every iteration, update
this dictionary.

Create another dictionary with an explorer class. The explorer looks at the
storm dictionary to see where it can move at any given moment. If there are
multiple possibilities, it clones itself and goes to all of them.

Part 1 goes quickly. The return trip on part 2 is very slow for some reason.
"""

from collections import defaultdict
DATA = 'data202224.txt'
# DATA = 'testdata202224.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetGrid(lines):
  """Create a grid from the input lines."""
  grid_dict = defaultdict(lambda: [])
  for row, line in enumerate(lines):
    for col, char in enumerate(line):
      # ignore '.' and ' ' characters
      if char in ['#', '>', '<', '^', 'v']:
        grid_dict[(col, row)] = char
  return grid_dict


def GridMinMax(grid):
  """Minimum and maximum grid coordinates, for printing."""
  x_all = [x for x, y in grid]
  y_all = [y for x, y in grid]
  min_x = min(x_all)
  min_y = min(y_all)
  max_x = max(x_all)
  max_y = max(y_all)
  return min_x, min_y, max_x, max_y


def PrintGrid(grid, overlay=None, default_char='.'):
  """Print the grid using only as much space as necessary."""
  min_x, min_y, max_x, max_y = GridMinMax(grid)
  for y in range(min_y, max_y + 1):
    row_str = ''
    for x in range(min_x, max_x + 1):
      if overlay and (x, y) in overlay and overlay[(x, y)]:
        if len(overlay[(x, y)]) == 1:
          char = overlay[(x, y)][0].symbol
        else:
          char = str(len(overlay[(x, y)]))
      else:
        char = grid.get((x, y), default_char)
      row_str += char
    print(row_str)


class Blizzard():
  """A blizzard class. All it does is move in one direction until it reaches
     the end of the world, then starts again at the other side; and it keeps
     track of where it is."""

  def __init__(self, coords, symbol, grid_min_max):
    self.coord = coords
    self.symbol = symbol
    self.min_x, self.min_y, self.max_x, self.max_y = grid_min_max
    self.move_op = self.GetMoveOp(symbol)

  def GetMoveOp(self, symbol):
    """Each symbol is associated with a direction and a way to move."""
    op_map = {'^': self.MoveUp,
              'v': self.MoveDown,
              '>': self.MoveRight,
              '<': self.MoveLeft}
    return op_map[symbol]

  def Move(self, storm_grid):
    """Move self once step and update the storm_grid."""
    prev_coord = self.coord
    next_coord = self.move_op()
    self.coord = next_coord
    storm_grid[next_coord].append(self)
    storm_grid[prev_coord].remove(self)

  def MoveUp(self):
    """For ^ blizzards."""
    x, y = self.coord
    y = y - 1
    if y == self.min_y:
      y = self.max_y - 1
    return x, y

  def MoveDown(self):
    """For v blizzards."""
    x, y = self.coord
    y = y + 1
    if y == self.max_y:
      y = self.min_y + 1
    return x, y

  def MoveRight(self):
    """For > blizzards."""
    x, y = self.coord
    x = x + 1
    if x == self.max_x:
      x = self.min_x + 1
    return x, y

  def MoveLeft(self):
    """For < blizzards."""
    x, y = self.coord
    x = x - 1
    if x == self.min_x:
      x = self.max_x - 1
    return x, y

  def __str__(self):
    return f'{self.symbol}{self.coord}'


def GetInitialBlizzards(grid):
  """From the starting grid, create a list of blizzard objects."""
  grid_min_max = GridMinMax(grid)
  blizzard_list = []
  for coord in grid:
    if grid[coord] in ['^', '<', '>', 'v']:
      blizzard_list.append(Blizzard(coord, grid[coord], grid_min_max))
  return blizzard_list


class Explorer():
  """Explorer class that looks at neighbors to see if he can move."""
  def __init__(self, coord, grid, storm_grid):
    self.coord = coord
    self.storm_grid = storm_grid
    self.grid = grid

  def MoveableCells(self):
    """Unoccupied cells the explorer can move to."""
    x, y = self.coord
    possibles = [(x, y), (x + 1, y), (x - 1, y), (x, y + 1)]
    if y > 0:
      possibles.append((x, y - 1))
    return [i for i in possibles
            if i not in self.grid and
            not self.storm_grid[i]]

  def __str__(self):
    return f'{self.coord}'


def MoveBlizzards(blizzard_list, storm_grid):
  """Move every blizzard in the list."""
  for b in blizzard_list:
    b.Move(storm_grid)


def MoveExplorers(explorers_grid):
  """Move every explorer in the list. If an explorer can move to two different
     places, create new explorers and put them there."""
  explorers_list = list(explorers_grid.values())[:]

  for e in explorers_list:

    # cells you can move to, if not occupied, except by self
    moveable_cells = [i for i in e.MoveableCells() if i not in explorers_grid]
    if e.coord in e.MoveableCells() and e.coord not in moveable_cells:
      moveable_cells.append(e.coord)

    if not moveable_cells:
      # The explorer at {e.coord} is removed.'
      explorers_grid.pop(e.coord)
    elif len(moveable_cells) == 1 and moveable_cells[0] == e.coord:
      # The explorer at {e.coord} does not move.
      pass
    elif len(moveable_cells) == 1:
      # The explorer at {e.coord} moves to {moveable_cells[0]}.
      explorers_grid.pop(e.coord)
      e.coord = moveable_cells[0]
      explorers_grid[e.coord] = e
    elif len(moveable_cells) > 1:
      for cell in moveable_cells:
        if cell == e.coord:
          # The explorer at {e.coord} stays in place.
          continue
        # Create new explorer at {cell}.
        new_explorer = Explorer(cell, e.grid, e.storm_grid)
        explorers_grid[cell] = new_explorer
      if e.coord not in moveable_cells:
        explorers_grid.pop(e.coord)
    else:
      raise Exception


def Solve():
  """Solve both parts"""
  lines = GetData(DATA)
  max_y = len(lines) - 1
  max_x = len(lines[0]) - 1
  start = (1, 0)
  target = (max_x - 1, max_y)
  grid = GetGrid(lines)

  # create a list of blizzard objects
  blizzard_list = GetInitialBlizzards(grid)

  # create a storm grid with a list of blizzards for each coordinate
  storm_grid = defaultdict(lambda: [])
  for b in blizzard_list:
    storm_grid[b.coord].append(b)

  # clear the initial grid
  for b in blizzard_list:
    grid.pop(b.coord)

  # create an explorer
  explorers_grid = {}
  explorer = Explorer(start, grid, storm_grid)
  explorers_grid[start] = explorer

  minutes = 0
  while target not in explorers_grid:
    minutes += 1
    MoveBlizzards(blizzard_list, storm_grid)
    MoveExplorers(explorers_grid)
  print(f'Part 1: {minutes}')

  # part 2 go back
  explorers_grid = {}
  explorer = Explorer(target, grid, storm_grid)
  explorers_grid[target] = explorer

  while start not in explorers_grid:
    minutes += 1
    MoveBlizzards(blizzard_list, storm_grid)
    MoveExplorers(explorers_grid)

  # part 2 go forward
  explorers_grid = {}
  explorer = Explorer(start, grid, storm_grid)
  explorers_grid[start] = explorer

  while target not in explorers_grid:
    minutes += 1
    MoveBlizzards(blizzard_list, storm_grid)
    MoveExplorers(explorers_grid)
  print(f'Part 2: {minutes}')


def main():
  """main"""
  Solve()


if __name__ == '__main__':
  main()
