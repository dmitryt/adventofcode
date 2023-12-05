from pprint import pprint
from utils import file, array

filepath = 'input/3.txt'

def mark_cell_and_adjacents(matrix, i, j, mark = 'X'):
  coords = (
    (i, j - 1),
    (i - 1, j - 1),
    (i - 1, j),
    (i - 1, j + 1),
    (i, j + 1),
    (i + 1, j + 1),
    (i + 1, j),
    (i + 1, j - 1),
  )
  for c in coords:
    if c[0] < 0 or c[1] < 0 or c[0] >= len(matrix) or c[1] >= len(matrix[0]):
      continue
    matrix[c[0]][c[1]] = mark

def is_part_number(map_matrix: list, i: int, start: int, end: int) -> bool:
  if start == None or end == None:
    return False
  for j in range(start, end + 1):
    if map_matrix[i][j] == 'X':
      return True
  return False

def exec():
  result = []
  matrix = file.readIntoMatrix(filepath)
  map_matrix = array.create_empty_matrix(len(matrix), len(matrix[0]), '.')
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if (not matrix[i][j].isdigit() and matrix[i][j] != "."):
        mark_cell_and_adjacents(map_matrix, i, j)
        map_matrix[i][j] = matrix[i][j]
  for i in range(len(matrix)):
    last_num = [None, None]
    for j in range(len(matrix[i])):
      if matrix[i][j].isdigit():
        if last_num[0] is None:
          last_num[0] = j
        last_num[1] = j
      if not matrix[i][j].isdigit() or j == len(matrix[i]) - 1:
        if is_part_number(map_matrix, i, last_num[0], last_num[1]):
          num = int(''.join(matrix[i][last_num[0]:last_num[1] + 1]))
          result.append(num)
        last_num = [None, None]
  print("Result:", sum(result))
exec()