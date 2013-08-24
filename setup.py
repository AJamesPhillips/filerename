#!/usr/bin/env python3

start = 1872
num = 20

for i in range(start, start+num):
  with open('./images/DCSF{i}.jpg'.format(i=i), 'a+') as f:
    f.write('image' + str(i))

print('done')
