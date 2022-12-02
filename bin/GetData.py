#!/usr/bin/python3
# $Id$
"""
Grab the data for a given day and put it in file dataDDYYYY.txt

Usage: GetData.py <day> <year>

 * Create data<YEAR><DAY>.txt
 * Requires valid session cookie in file SessionCookie.
 * Pulls data via curl, with contact info in the user agent field.
 * Test with 'GetData.py 0 0' which will try to pull from TEST_URL.
"""

import os
import subprocess
import sys

# look at your chrome cookies from AOC web site
# inspect -> application -> cookies -> session

COOKIE_FILE = f'{os.path.dirname(__file__)}/SessionCookie'
TEST_URL = 'redacted'
CONTACT = 'redacted'
YEAR = 2022
DAY = 1


def ReadCookie(cookie_file):
  with open(cookie_file, 'r') as fh:
    cookie = next(fh).strip()
  return cookie


def GetUrl(day=0, year=0):
  """Given a day and year, construct the URL."""
  if day == 0:
    return TEST_URL
  return f'https://adventofcode.com/{year}/day/{day}/input'


def UserAgent():
  """Return a UserAgent string. curl version determined dynamically."""
  cmd = ['/usr/bin/curl', '-V']
  raw_data = subprocess.check_output(cmd).decode('utf-8').strip()
  curl_version = raw_data.split()[1]
  return f'curl/{curl_version} from {CONTACT}' 


def GetRawInput(session_cookie, target_url):
  """use curl to get input"""
  cmd = ['/usr/bin/curl',
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
  year = YEAR if len(argv) <=2 else int(argv[2])
  filename = f'data{year}{day:>02}.txt'
  if os.path.exists(filename):
    print(f'{filename} already exists')
    sys.exit()

  with open(filename, 'w') as fh:
    aoc_cookie = ReadCookie(COOKIE_FILE)
    target_url = GetUrl(day, year)
    fh.write(GetRawInput(aoc_cookie, target_url))
    fh.write('\n')

  # create empty file if it doesn't exit
  with open(f'testdata{year}{day:>02}.txt', 'a') as fh:
    pass


if __name__ == '__main__':
  main(sys.argv)
