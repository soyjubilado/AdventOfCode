def h_test(testcases, func, unpack=False):
  """Lame ass testing framework because I like verbose test output."""
  print(f'\n--- testing {func.__name__} ---')
  failures = 0
  for c, expected in testcases:
    actual = func(c) if not unpack else func(*c)
    if actual == expected:
      passing = 'pass'
    else:
      passing = 'fail'
      failures += 1
    suffix = f'expected {expected}' if passing != 'pass' else ''
    print(f'{passing}: {c} -> {actual} {suffix}')
  print(f'{failures}/{len(testcases)} failures for {func.__name__}')
  return failures

