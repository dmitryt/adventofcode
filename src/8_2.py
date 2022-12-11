filepath = 'input/8.txt'

def init_traverse(matrix, start_i, start_j):
  def exec(di, dj):
    if start_i == 0 or start_j == 0 or start_i == len(matrix) - 1 or start_j == len(matrix[start_i]) - 1:
      return 0
    distance = 0
    if dj == 0:
      maxi = len(matrix) if di > 0 else -1
      for i in range(start_i + di, maxi, di):
        distance += 1
        if matrix[i][start_j] >= matrix[start_i][start_j]:
          break
    if di == 0:
      maxj = len(matrix[start_i]) if dj > 0 else -1
      for j in range(start_j + dj, maxj, dj):
        distance += 1
        if matrix[start_i][j] >= matrix[start_i][start_j]:
          break
    return distance
  return exec

def exec():
  with open(filepath, encoding="utf-8") as f:
    matrix = []
    i = 0
    max_scenic_score = 0
    for line in f.readlines():
      ln = line[:-1]
      matrix.append([])
      for item in ln:
        matrix[i].append(int(item))
      i += 1
    for i in range(0, len(matrix)):
      for j in range(0, len(matrix[i])):
        traverse = init_traverse(matrix, i, j)
        scenic_score = traverse(0, 1) * traverse(1, 0) * traverse(0, -1) * traverse(-1, 0)
        if scenic_score > max_scenic_score:
          max_scenic_score = scenic_score
    print("Result:", max_scenic_score)
exec()