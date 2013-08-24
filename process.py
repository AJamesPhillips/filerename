#!/usr/bin/env python3

import os
import re
import sys

start = 1
match = '^DCSF'
output = ''

def pad(txt):
  return str(txt).rjust(4, '0')

def name(num):
  return output + pad(num) + '.jpg'

if len(sys.argv) > 1:
  if sys.argv[1] in ['--help']:
    print("""
    Usage:  accepts the following arguments
      --help  displays this help message
      --start=N  where N is the number to start renaming files as
                 for example if you already had 11 files name holiday0001.jpg to holiday0011.jpg
                 and wanted to rename the files DSCF0012.jpg and DSCF0013.jpg then you would want
                 these to be renamed to holiday0012.jpg and holiday0013.jpg so you'd provide the
                 arugument --start=12
                 Defaults to 1
      -s=N  same as --start, e.g. provide:  -o=12
      --match=S   where S is the regular expression that will match your files.  the ^ means it
                  matches from the start of the filename whereas just 'DCSF' would match any
                  filename containing DCSF
                  Defaults to '^DCSF'
      -m=S  same as --match
      --output=S  where S is the name of the output file.  e.g. --output=holiday would make the output
                  files have the names holiday0001.jpg etc
                  Defaults to nothing
      -o=S  same as --output  e.g. -o='yeah and?!'
    """)
  else:
    for arg in sys.argv:
      start_m = re.search('^--start=(.+)', arg)
      s_m = re.search('^-s=(.+)', arg)
      if start_m:
        start = int(start_m.groups()[0])
      elif s_m:
        start = int(s_m.groups()[0])

      match_m = re.search('^--match=(.+)', arg)
      m_m = re.search('^-m=(.+)', arg)
      if match_m:
        match = match_m.groups()[0]
      elif m_m:
        match = m_m.groups()[0]

      output_m = re.search('^--output=(.+)', arg)
      o_m = re.search('^-o=(.+)', arg)
      if output_m:
        output = output_m.groups()[0]
      elif o_m:
        output = o_m.groups()[0]
    print('Matching files with "{match}", and will rename to e.g.: {name}'.format(match=match, name=name(start)))


matched = 0
for filename in os.listdir('.'):
  if re.search(match, filename):
    os.rename(filename, name(start))
    start += 1
    matched += 1
print('Matched {matched} files'.format(matched=matched))
