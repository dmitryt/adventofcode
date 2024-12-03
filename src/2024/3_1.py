from utils import file
import re

filepath = 'input/3_dev.txt'

def exec():
  expr = file.read(filepath)
  res = 0
  for key in re.findall(r'mul\((\d+,\d+)\)', expr):
    [n1, n2] = map(lambda x: int(x), key.split(','))
    res += n1 * n2
  print(res)
exec()
