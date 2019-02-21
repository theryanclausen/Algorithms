#!/usr/bin/python

import sys
rps = [['rock'], ['paper'], ['scissors']]

def rps_appender(l):
  return [[*l, rps[0][0]], [*l, rps[1][0]], [*l, rps[2][0]]]

def rock_paper_scissors(n):
  result = [[]]
  while n > 0:
    length = len(result)
    temp = []
    for x in result:
       temp.extend(rps_appender(x))
    n = n - 1
    result = temp
  return result

print(rock_paper_scissors(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[2])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')