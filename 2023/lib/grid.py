"""Grid structure and related functions."""

def Grid(lines):
  """Return a dictionary of coordinates."""
  grid = {}
  for y, line in enumerate(lines):
    for x, char in enumerate(line):
      grid[(x, y)] = char
  return grid


def MinMaxXY(grid):
  """Return min_x, max_x, min_y, max_y"""
  x_all = [x for x, y in grid]
  y_all = [y for x, y in grid]
  return min(x_all), max(x_all), min(y_all), max(y_all)


def PrintGrid(grid, default_char='.'):
  """Swiped from previous year."""
  min_x, max_x, min_y, max_y = MinMaxXY(grid)
  for y in range(min_y, max_y + 1):
    row_str = ''
    for x in range(min_x, max_x + 1):
      row_str += f'{str(grid.get((x, y), default_char))}'
    print(row_str)


class GridWrap():
  """Wrapper class for grid, that acts like a grid dictionary."""

  def __init__(self, lines, name=None, default_char='.'):
    """If you give it a name, print that instead of the dict."""
    self.grid = Grid(lines)
    self.name = name if name else lines[0]
    self.default_char = default_char

  def __getitem__(self, key):
    """Allow access by key, just like a dict."""
    return self.grid[key]

  def __iter__(self):
    """Return dict keys as an interable."""
    return iter(self.grid.keys())

  def __repr__(self):
    return self.name

  def as_str(self):
    """String representation of the grid."""
    retval_list = []
    min_x, max_x, min_y, max_y = MinMaxXY(self.grid)
    for y in range(min_y, max_y + 1):
      row_str = ''
      for x in range(min_x, max_x + 1):
        row_str += f'{str(self.grid.get((x, y), self.default_char))}'
      retval_list.append(row_str)
    return '\n'.join(retval_list)

  def items(self):
    """Return dictionary items."""
    return self.grid.items()

  def keys(self):
    """Return dictionary keys."""
    return self.grid.keys()

  def values(self):
    """Return dictionary values."""
    return self.grid.values()
