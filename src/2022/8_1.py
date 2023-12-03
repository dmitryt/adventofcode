filepath = 'input/8.txt'

def exec():
  with open(filepath, encoding="utf-8") as f:
    # item:
    #   - value: item value
    #   - visibility: max visibility for the following directions [top, right, bottom, left]
    matrix = []
    i = 0
    for line in f.readlines():
      ln = line[:-1]
      matrix.append([])
      j = 0
      for item in ln:
        top = max(matrix[i - 1][j]['value'], matrix[i - 1][j]['visibility'][0]) if i > 0 else -1
        left = max(matrix[i][j - 1]['value'], matrix[i][j - 1]['visibility'][3]) if j > 0 else -1
        matrix[i].append({"value": int(item), "visibility": [top,-1,-1,left]})
        j += 1
      i += 1
    result = []
    for i in range(len(matrix) - 1, -1, -1):
      for j in range(len(matrix[i]) - 1, -1, -1):
        right = max(matrix[i][j + 1]['value'], matrix[i][j + 1]['visibility'][1]) if j < len(matrix[i]) - 1 else -1
        matrix[i][j]['visibility'][1] = right
        bottom = max(matrix[i + 1][j]['value'], matrix[i + 1][j]['visibility'][2]) if i < len(matrix) - 1 else -1
        matrix[i][j]['visibility'][2] = bottom
        if matrix[i][j]['value'] > min(matrix[i][j]['visibility']):
          result.append((matrix[i][j]['value'], i, j))
    print(len(result))
exec()