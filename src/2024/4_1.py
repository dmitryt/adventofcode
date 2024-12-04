from utils import file

filepath = 'input/4.txt'

def find_word(matrix, coords, dir, depth):
  word = "XMAS"
  if depth == len(word):
    return True
  
  is_out_borders = coords[0] < 0 or coords[1] < 0 or coords[0] >= len(matrix) or coords[1] >= len(matrix[0])
  
  if is_out_borders or matrix[coords[0]][coords[1]] != word[depth]:
    return False

  return find_word(matrix, (coords[0] + dir[0], coords[1] + dir[1]), dir, depth + 1)


def exec():
  matrix = file.readIntoMatrix(filepath)
  dirs = ((0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1, 0), (-1,1))
  cnt = 0
  for i, row in enumerate(matrix):
    for j, char in enumerate(row):
      if char == "X":
        for dir in dirs:
          if find_word(matrix, (i, j), dir, 0):
            cnt += 1
  print(cnt)
exec()
