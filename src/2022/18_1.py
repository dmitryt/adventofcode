filepath = 'input/18.txt'

def init():
  matrix = []
  with open(filepath, encoding="utf-8") as f:
    max_x = max_y = max_z = 0
    for line in f.readlines():
      x, y, z = list(map(lambda x: int(x), line[:-1].split(',')))
      if x > max_x:
        max_x = x
      if y > max_y:
        max_y = y
      if z > max_z:
        max_z = z
    for x in range(max_x):
      matrix.append([])
      for y in range(max_y):
        matrix[x].append([])
        for z in range(max_z):
          matrix[x][y].append(None)
  with open(filepath, encoding="utf-8") as f:
    for line in f.readlines():
      x, y, z = list(map(lambda x: int(x), line[:-1].split(',')))
      matrix[x-1][y-1][z-1] = True
  return matrix

def exec():
  matrix = init()
  print(matrix)
  cnt = 0
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      for k in range(len(matrix[i][j])):
        if matrix[i][j][k] is None:
          continue
        if k == 0 or matrix[i][j][k - 1] is None:
          cnt += 1
        if k == len(matrix[i][j]) - 1 or matrix[i][j][k + 1] is None:
          cnt += 1
        if j == 0 or matrix[i][j - 1][k] is None:
          cnt += 1
        if j == len(matrix[i]) - 1 or matrix[i][j + 1][k] is None:
          cnt += 1
        if i == 0 or matrix[i - 1][j][k] is None:
          cnt += 1
        if i == len(matrix) - 1 or matrix[i + 1][j][k] is None:
          cnt += 1
  print("Result:", cnt)
exec()