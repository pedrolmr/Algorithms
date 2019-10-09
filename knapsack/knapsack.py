#!/usr/bin/python
# N C/S V
# 1 42 81
# 2 42 42
# 3 68 56
# 4 68 25
# 5 77 14
# 6 57 63
# 7 17 75
# 8 19 41
# 9 94 19
# 10 34 12

# The program should also take as input a total size, which can just be a number passed from the command line. So execution may look like this: python knapsack.py input.txt 100

# Items to select: 2, 8, 10
# Total cost: 98
# Total value: 117

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  pass

f = open("data/small1.txt", "r")
f1 = f.readlines()
for i in f1:
  print(i[2])
  # li = [i[0], i[1], i[2]]
  # element = Item(i[0], i[1], i[2])
  # print(element)

# if __name__ == '__main__':
#   if len(sys.argv) > 1:
#     capacity = int(sys.argv[2])
#     file_location = sys.argv[1].strip()
#     file_contents = open(file_location, 'r')
#     items = []

#     for line in file_contents.readlines():
#       data = line.rstrip().split()
#       items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
#     file_contents.close()
#     print(knapsack_solver(items, capacity))
#   else:
#     print('Usage: knapsack.py [filename] [capacity]')
