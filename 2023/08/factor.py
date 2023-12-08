#!/usr/bin/env python3


from subprocess import check_output
import sys


def factors(n):
  """Return a list of prime factors of n. Requires factor binary on system."""
  cmd = ['factor', f'{n}']
  output_bytes = check_output(cmd)
  output_string = output_bytes.decode('utf-8').strip()
  factors_part = output_string.split(':')[1].split()
  return [int(i) for i in factors_part]


def main(argv):
  if len(argv) < 2:
    print('Requires argument')
    return
  n = int(argv[1])
  print(f'Factors of {n}: {factors(n)}')


if __name__ == '__main__':
  main(sys.argv)
