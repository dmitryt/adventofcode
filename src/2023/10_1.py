import re
from utils import file

filepath = 'input/10.txt'

visited = {}

def get_next_steps(coords, matrix, steps):
  connectors = {
    'L': ['L', 'F', '-'],
    'R': ['J', '7', '-'],
    'T': ['7', 'F', '|'],
    'B': ['L', 'J', '|'],
  }

  result = []
  possible_steps = (
    (coords[0], coords[1] - 1, connectors['L']),
    (coords[0], coords[1] + 1, connectors['R']),
    (coords[0] - 1, coords[1], connectors['T']),
    (coords[0] + 1, coords[1], connectors['B']),
  )
  for step in possible_steps:
    i, j, connectors = step
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[i]) or (i, j) in visited:
      continue
    for c in connectors:
      if matrix[i][j] == c:
        result.append((i, j, steps + 1))
        break
  return result

def exec():
  matrix = []
  start_coords = None
  def processLine(line) -> None:
    nonlocal start_coords
    matrix.append(line[:-1] if line[-1] == '\n' else line)
    start_index = line.find('S')
    if start_index != -1:
      start_coords = (len(matrix) - 1, start_index)


  file.processFileLine(filepath, processLine)

  result = None
  queue = get_next_steps(start_coords, matrix, 0)
  while len(queue) > 0:
    # print(queue)
    new_coords = queue.pop(0)
    if matrix[new_coords[0]][new_coords[1]] == 'S':
      result = new_coords[2]
      break
    steps = new_coords[2]
    queue += get_next_steps(new_coords, matrix, steps)
    visited[(new_coords[0], new_coords[1])] = True
    if steps % 100 == 0:
      print(steps)
    if len(queue) == 0:
      result = steps
  print("Result:", result)

exec()