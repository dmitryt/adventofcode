from utils import file
import re

filepath = 'input/1.txt'

def exec():
  first = []
  second = []
  def process(line):
    nonlocal first
    nonlocal second
    res = re.split(r'\s+', line[:-1])
    first += [int(res[0])]
    second += [int(res[1])]

  file.processFile(filepath, process)
  first = sorted(first)
  second = sorted(second)

  distance = 0
  for i in range(len(first)):
    distance += abs(first[i] - second[i])

  print(distance)

exec()
