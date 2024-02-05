def Grid(lines):
  """Return a dictionary of coordinates."""
  grid = {}
  for y, line in enumerate(lines):
    for x, char in enumerate(line):
      grid[(x, y)] = char
  return grid


def PrintGrid(grid, default_char='.'):
  """Swiped from previous year."""
  x_all = [x for x, y in grid]
  y_all = [y for x, y in grid]
  max_x = max(x_all)
  max_y = max(y_all)
  min_x = min(x_all)
  min_y = min(y_all)
  for y in range(min_y, max_y + 1):
    row_str = ''
    for x in range(min_x, max_x + 1):
      row_str += f'{str(grid.get((x, y), default_char))}'
    print(row_str)

