#!/usr/bin/python

import sys

stair_cache = {}

def climbing_stairs(n, cache=None):
  if n in stair_cache:
    return stair_cache[n]
  value = None
  if n == 0 or n == 1:
    value = 1
  elif n == 2:
    value = 2
  elif n > 2:
    value = climbing_stairs(n - 1) + climbing_stairs(n - 2) + climbing_stairs(n - 3)
  stair_cache[n] = value
  return value

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')