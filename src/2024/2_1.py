from utils import file
import re

filepath = 'input/2.txt'

def exec():
  matrix = []
  def process(line):
    matrix.append(
      list(map(lambda x: int(x), re.split(r'\s+', line[:-1])))
    )
  file.processFile(filepath, process)
  
  cnt = 0

  for row in matrix:
    is_safe = True
    dir = None
    prev = row[0]
    for char in row[1:]:
      if dir is None:
        dir = 1 if char > prev else -1
      diff = char - prev
      is_safe = abs(diff) <= 3 and diff * dir > 0
      if is_safe is False:
        break

      prev = char
      
    if is_safe:
      cnt += 1


  print(cnt)

exec()
