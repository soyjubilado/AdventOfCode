#!/usr/bin/env python3

from prog202305 import TransformMap, SplitRange


def testSplitRange():
  self_maps = [TransformMap(120, 20, 10),
               TransformMap(230, 30, 5),
               TransformMap(335, 35, 5)]
  test_cases = [((19, 3), [(19, 1), (20, 2)]),
                ((18, 4), [(18, 2), (20, 2)]),
                ((12, 4), [(12, 4)]),
                ((20, 4), [(20, 4)]),
                ((19, 15), [(19, 1), (20, 10), (30, 4)]),
                ((40, 4), [(40, 4)]),
                ((39, 4), [(39, 1), (40, 3)]),
                ((39, 1), [(39, 1)]),
                ((39, 2), [(39, 1), (40, 1)]),
                ((40, 1), [(40, 1)]),
                ((18, 25), [(18, 2), (20, 10), (30, 5), (35, 5), (40, 3)]),
               ]
  for t_range, expected in test_cases:
    actual = SplitRange(t_range, self_maps)
    passing = 'pass' if actual == expected else 'fail'
    expectation = f'(expected {expected})' if passing == 'fail' else ''
    print(f'{passing}: {t_range} -> {actual} {expectation}')


testSplitRange()
