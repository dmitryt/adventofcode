from utils import file

filepath = 'input/4.txt'

def get_char(matrix, coords):
  is_out_borders = coords[0] < 0 or coords[1] < 0 or coords[0] >= len(matrix) or coords[1] >= len(matrix[0])
  
  if is_out_borders:
    return None
  
  return matrix[coords[0]][coords[1]]


def exec():
  matrix = file.readIntoMatrix(filepath)
  cnt = 0
  for i, row in enumerate(matrix):
    for j, char in enumerate(row):
      if char == "A":
        t_l = get_char(matrix, (i - 1, j - 1))
        t_r = get_char(matrix, (i - 1, j + 1))
        b_l = get_char(matrix, (i + 1, j - 1))
        b_r = get_char(matrix, (i + 1, j + 1))
        if t_l is None or t_r is None or b_l is None or b_r is None:
          continue
        expr = t_l + t_r + b_l + b_r 
        if expr == "SSMM" or expr == "MMSS" or expr == "SMSM" or expr == "MSMS":
          cnt += 1
  print(cnt)
exec()
