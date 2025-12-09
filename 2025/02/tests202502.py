#!/usr/bin/env python3

import re
from h_test import h_test

INVALID_RE = re.compile(r'^([0-9]+)\1{1,}$')

def IsInvalid(num):
  answer = None
  match = INVALID_RE.match(str(num))
  if match:
    answer = True
    print(f'{num} -> {match.groups()}')
  else:
    print(f'{str(num)} -> no match')
    answer = False
  return answer


def testIsInvalid():
  cases = [[1, False],
           [22, True],
           [222, True],
           [232, False],
           [332, False],
           [223, False],
           [2233, False],
           [123123123, True],
           [123456, False],
           [1188511885, True],
           [222222, True],
           [446446, True],
           [38593859, True],
           [565656, True],
           [824824824, True],
          ]
  h_test(cases, IsInvalid)


testIsInvalid()
