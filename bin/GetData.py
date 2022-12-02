#!/usr/bin/python3
# $Id$
"""
Grab the data for a given day and put it in file dataDDYYYY.txt

Usage: GetData.py <day> <year>

 * Create data<YEAR><DAY>.txt
 * Requires the following definitions in GetDataConfig.py:
    - SESSION_COOKIE: an adventofcode session cookie
    - CONTACT: an email address for the user agent
    - TEST_URL: a test URL
 * Pulls data via curl, with contact info in the user agent field.
 * Test with 'GetData.py 0 0' which will try to pull from TEST_URL.
"""

import os
import subprocess
import sys
from GetDataConfig import SESSION_COOKIE, CONTACT, TEST_URL


CURL = '/usr/bin/curl'
DAY = 1
YEAR = 2022


def GetUrl(day=0, year=0):
  """Given a day and year, construct the URL."""
  if day == 0:
    return TEST_URL
  return f'https://adventofcode.com/{year}/day/{day}/input'


def UserAgent():
  """Return a UserAgent string. curl version determined dynamically."""
  cmd = [CURL, '-V']
  raw_data = subprocess.check_output(cmd).decode('utf-8').strip()
  curl_version = raw_data.split()[1]
  return f'curl/{curl_version} from {CONTACT}'


def GetRawInput(session_cookie, target_url):
  """use curl to get input"""
  cmd = [CURL,
         target_url,
         '-X', 'GET', '-H',
         f'Cookie: session={session_cookie}',
         '-A',
         UserAgent(),
        ]

  raw_data = subprocess.check_output(cmd).decode('utf-8').strip()
  return raw_data


def main(argv):
  if len(argv) < 2:
    print(f'Usage: {os.path.basename(__file__)} <day> [<year>]')
    sys.exit()
  day = DAY if len(argv) <= 1 else int(argv[1])
  year = YEAR if len(argv) <= 2 else int(argv[2])
  filename = f'data{year}{day:>02}.txt'
  if os.path.exists(filename):
    print(f'{filename} already exists')
    sys.exit()

  with open(filename, 'w') as fh:
    target_url = GetUrl(day, year)
    fh.write(GetRawInput(SESSION_COOKIE, target_url))
    fh.write('\n')

  # create empty file if it doesn't exit
  with open(f'testdata{year}{day:>02}.txt', 'a') as fh:
    pass


if __name__ == '__main__':
  main(sys.argv)
