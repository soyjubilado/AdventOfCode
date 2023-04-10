import re
REGEX = re.compile('([A-Z]*)\(([0-9]+)x([0-9]+)\)(.*)')

def NewExtractParts(line):
  """Alternate version of ExtractParts() using regex."""
  prefix, count, repeat, end_str = REGEX.match(line).groups()
  substr = end_str[:int(count)]
  suffix = end_str[int(count):]
  return prefix, int(repeat), substr, suffix
