import re
from pprint import pprint
from utils import file

filepath = 'input/11_dev.txt'

def expand_universe(matrix, empty_rows, empty_columns):
  matrix_len = len(matrix)
  cnt = 0
  for j, flag in enumerate(empty_columns):
    if flag == True:
      for i in range(matrix_len):
        matrix[i].insert(j + cnt, '.')
      cnt += 1

  cnt = 0
  empty_row = ['.' for _ in range(len(matrix[0]))]
  for i, flag in enumerate(empty_rows):
    if flag == True:
      matrix.insert(i + cnt, empty_row)
      cnt += 1

def exec():
  result = []
  matrix = file.readIntoMatrix(filepath)
  empty_rows = [True for _ in range(len(matrix))]
  empty_columns = [True for _ in range(len(matrix[0]))]

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      is_empty = matrix[i][j] == '.'
      empty_rows[i] = empty_rows[i] and is_empty
      empty_columns[j] = empty_columns[j] and is_empty

  expand_universe(matrix, empty_rows, empty_columns)

  galaxies = []
  distancies = []
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == '#':
        galaxies.append((i, j))

  print(galaxies)
  for i in range(len(galaxies) - 1):
    base = galaxies[i]
    for j in range(i + 1, len(galaxies)):
      galaxy = galaxies[j]
      distancies.append(abs(base[0] - galaxy[0]) + abs(base[1] - galaxy[1]))

  print("Result:", sum(distancies))

exec()