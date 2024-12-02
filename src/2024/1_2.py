from utils import file
import re

filepath = 'input/1.txt'

def exec():
  first = []
  second = {}
  def process(line):
    nonlocal first
    nonlocal second
    res = list(map(lambda x: int(x), re.split(r'\s+', line[:-1])))
    first += [res[0]]
    if res[1] not in second:
      second[res[1]] = 0
    
    second[res[1]] += 1

  file.processFile(filepath, process)

  result = 0
  for i in range(len(first)):
    result += first[i] * second.get(first[i], 0)

  print(result)

exec()
