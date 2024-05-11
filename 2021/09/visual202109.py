#!/usr/bin/python3
# visualization of sea floor for 2021 day 9

from textwrap import dedent
DATA = 'data202109.txt'

def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines

def PrintHead():
  header = dedent("""<html><head></head><body>
                     <table>
                     <tr>"""
                 )
  print(header)


COLOR = {'0': '#ff0000',
         '1': '#ee1100',
         '2': '#dd2211',
         '3': '#bb4433',
         '4': '#997744',
         '5': '#447799',
         '6': '#3344bb',
         '7': '#1122dd',
         '8': '#0011ee',
         '9': '#ffffff',
        }


def main():
  lines = GetData(DATA)
  PrintHead()
  for line in lines:
    for cell in line:
      print(f'<td bgcolor="{COLOR[cell]}">')
    print('</tr>')
  print('</table></body></html>')

main()
