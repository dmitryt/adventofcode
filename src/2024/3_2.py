from utils import file
import re

filepath = 'input/3.txt'

def exec():
  expr = file.read(filepath)
  res = 0
  is_enabled = True
  for key in re.findall(r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)', expr):
    if key == "don't()":
      is_enabled = False
    elif key == "do()":
      is_enabled = True
    elif is_enabled:
      key = re.sub(r'mul\((.*?)\)', lambda x: x.group(1), key)
      [n1, n2] = map(lambda x: int(x), key.split(','))
      res += n1 * n2
  print(res)
exec()
