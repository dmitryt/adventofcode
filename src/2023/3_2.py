from pprint import pprint
from utils import file, array

filepath = 'input/3.txt'

EMPTY_CELL = None

def mark_cell_and_adjacents(matrix, i, j, mark = EMPTY_CELL):
  coords = (
    (i, j),
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

def get_adjacent_star(map_matrix: list, i: int, start: int, end: int) -> tuple:
  if start == None or end == None:
    return None
  for j in range(start, end + 1):
    if map_matrix[i][j] != EMPTY_CELL:
      return map_matrix[i][j]
  return None

def exec():
  result = []
  groupedNumbers = {}
  matrix = file.readIntoMatrix(filepath)
  map_matrix = array.create_empty_matrix(len(matrix), len(matrix[0]))
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if (matrix[i][j] == "*"):
        mark_cell_and_adjacents(map_matrix, i, j, (i, j))
  # pprint(map_matrix)
  for i in range(len(matrix)):
    last_num = [None, None]
    for j in range(len(matrix[i])):
      if matrix[i][j].isdigit():
        if last_num[0] is None:
          last_num[0] = j
        last_num[1] = j
      if not matrix[i][j].isdigit() or j == len(matrix[i]) - 1:
        adjacent_star = get_adjacent_star(map_matrix, i, last_num[0], last_num[1])
        if adjacent_star is not None:
          if not adjacent_star in groupedNumbers:
            groupedNumbers[adjacent_star] = []
          num = int(''.join(matrix[i][last_num[0]:last_num[1] + 1]))
          groupedNumbers[adjacent_star].append(num)
        last_num = [None, None]
  for _, value in groupedNumbers.items():
    if len(value) > 1:
      result.append(value[0] * value[1])
  print("Result:", sum(result))
exec()