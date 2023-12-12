import re
from pprint import pprint
from utils import file, dict

filepath = 'input/11.txt'

EXPAND_SIZE = 1000000

def expand(galaxies, arr, index):
  sorted(arr)
  cnt = 0
  for i in arr:
    for g in galaxies:
      if g[index] > i + cnt * (EXPAND_SIZE - 1):
        g[index] += EXPAND_SIZE - 1
    cnt += 1

def expand_universe(galaxies, empty_rows, empty_columns):
  expand(galaxies, empty_rows.keys(), 0)
  expand(galaxies, empty_columns.keys(), 1)

def exec():
  galaxies = []
  result = []
  matrix = file.readIntoMatrix(filepath)
  empty_rows = {}
  empty_columns = {}

  for i in range(len(matrix)):
    if i not in empty_rows:
      empty_rows[i] = True
    for j in range(len(matrix[i])):
      if j not in empty_columns:
        empty_columns[j] = True
      is_empty = matrix[i][j] == '.'
      empty_rows[i] = empty_rows[i] and is_empty
      empty_columns[j] = empty_columns[j] and is_empty
      if matrix[i][j] == '#':
        galaxies.append([i, j])

  expand_universe(
    galaxies,
    dict.clean_empty_values(empty_rows),
    dict.clean_empty_values(empty_columns),
  )

  distancies = []

  for i in range(len(galaxies) - 1):
    base = galaxies[i]
    for j in range(i + 1, len(galaxies)):
      galaxy = galaxies[j]
      distancies.append(abs(base[0] - galaxy[0]) + abs(base[1] - galaxy[1]))

  print("Result:", sum(distancies))

exec()