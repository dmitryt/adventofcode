filepath = 'input/12.txt'

directions = (
  (0, 1),
  (0, -1),
  (1, 0),
  (-1, 0),
)

def init():
  matrix = []
  start_coords = [-1, -1]
  with open(filepath, encoding="utf-8") as f:
    i = 0
    for line in f.readlines():
      ln = line[:-1]
      matrix.append([])
      for j in range(len(ln)):
        if ln[j] == 'S':
          start_coords = [i, j]
        matrix[i].append({"value": ln[j], "steps": float("inf")})
      i += 1
  return matrix, start_coords

def exec():
  def get_char(coords):
    [i, j] = coords
    return matrix[i][j]['value']

  def get_elevation(coords):
    char = get_char(coords)
    if char == 'S':
      char = 'a'
    if char == 'E':
      char = 'z'
    return ord(char)

  def is_point_outside(coords):
    [i, j] = coords
    return i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i])

  matrix, start_coords = init()
  queue = [(start_coords, 0)]
  result = float('inf')
  iterations = 0
  while len(queue) > 0:
    (coords, steps) = queue.pop(0)
    iterations += 1
    # print("Processing:", str(coords), steps)
    if get_char(coords) == 'E':
      result = min(result, steps)
    for (di, dj) in directions:
      new_coords = (coords[0] + di, coords[1] + dj)
      if is_point_outside(new_coords) or matrix[new_coords[0]][new_coords[1]]['steps'] <= steps + 1:
        continue
      if get_elevation(new_coords) - get_elevation(coords) > 1:
        continue
      matrix[new_coords[0]][new_coords[1]]['steps'] = steps + 1
      queue.append((new_coords, steps + 1))
  print(result, iterations)
exec()