#!/usr/bin/python3
#file created 2022-Dec-06 20:57
"""https://adventofcode.com/2022/day/7

Used the data input to build a tree of Files and Dirs. Then used recursion
to traverse the tree and get the answers.
"""
from collections import defaultdict

DATA = 'data202207.txt'

class DestDirectoryNotFound(Exception):
  """Exception thrown when you want to cd to a nonexistent subdirectory."""


def GetData(datafile):
  """Read the data input and return a list of strings."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return iter(lines)


class File():
  """Object representing a file in the tree."""
  def __init__(self, size, name):
    self.size = int(size)
    self.name = name

  def __str__(self):
    return f'{self.name} (file, size={self.size})'

  def Print(self, level=0):
    indent = ' ' * level
    print(f'{indent} - {self}')


class Dir():
  """Object representing a directory in the tree."""
  def __init__(self, name, parent=None):
    self.name = name
    self.contents = []
    self.parent = parent

  def __str__(self):
    return f'{self.name}'

  def Print(self, level=0):
    indent = ' ' * level
    print(f'{indent} - {self}')
    for i in self.contents:
      i.Print(level+1)

  def Subdirs(self):
    """Return a list of objects: all the directories below this one."""
    subdirs = [d for d in self.contents if isinstance(d, Dir)]
    all_dirs = subdirs[:]
    for d in subdirs:
      all_dirs.extend(d.Subdirs())
    return all_dirs

  def Size(self):
    """Return the sum of all the file sizes in this directory, plus the
       sum of the sizes of all subdirectories."""
    files = [f.size for f in self.contents if isinstance(f, File)]
    dirs = [d for d in self.contents if isinstance(d, Dir)]
    this_dir_size = sum(files)
    return this_dir_size + sum([d.Size() for d in dirs])


def GetDestPtr(ptr, current_line):
  """Given the current directory, and a line with '$ cd <dest>', return a
     reference to the new working directory."""
  dest = current_line.split()[-1]
  if dest == '..':
    return ptr.parent

  for i in ptr.contents:
    if i.name == dest:
      assert not isinstance(i, File)
      return i
  raise DestDirectoryNotFound


def NewContent(ptr, current_line):
  """Given a current directory ptr, and a line of ls output, create
     and return a new file or directory object"""
  if current_line.startswith('dir'):
    dest = current_line.split()[-1]
    return Dir(dest, parent=ptr)

  size, name = current_line.split()
  return File(size, name)


def BuildTree(lines):
  """Build the tree from the input data and return a reference to
     the root of the tree."""
  current_line = next(lines)
  root = Dir('/')
  ptr = root
  current_line = next(lines)

  try:
    while current_line:
      if current_line.startswith('$ cd'):
        new_ptr = GetDestPtr(ptr, current_line)
        ptr = new_ptr
        current_line = next(lines)
      elif current_line.startswith('$ ls'):
        current_line = next(lines)
        while not current_line.startswith('$'):
          ptr.contents.append(NewContent(ptr, current_line))
          current_line = next(lines)
  except StopIteration:
    pass

  return root


def Part1(lines):
  """Build the tree and grovel through it."""
  root = BuildTree(lines)
  answer = 0
  for d in root.Subdirs():
    d_size = d.Size()
    if d_size <= 100000:
      answer += d_size
  print(f'Part 1: {answer}')
  return root


def Part2(root):
  """root is the head of the tree from Part 1."""
  total_disk = 70000000
  disk_needed = 30000000
  disk_used = root.Size()
  current_free = total_disk - disk_used
  print('Part 2:')
  print(f'  root usage: {disk_used}')
  print(f'  current free space: {current_free}')
  need_free = disk_needed - current_free
  print(f'  need to delete: {need_free}')
  dir_vals = sorted([d.Size() for d in root.Subdirs()])

  answer = None
  for i in dir_vals:
    if i >= need_free:
      answer = i
      break
  print(f'  Part 2 answer: {answer}')


def CountCollisions(root):
  """Just for fun, count directory name collisions."""
  dir_name_dict = defaultdict(lambda: 0)
  for dir_obj in root.Subdirs():
    dir_name_dict[dir_obj.name] += 1
  print('Directory name collisions:')
  for name, count in dir_name_dict.items():
    if count > 1:
      print(f'  {name}: {count}')


def main():
  lines = GetData(DATA)
  root = Part1(lines)
  Part2(root)
  # CountCollisions(root)


if __name__ == '__main__':
  main()
