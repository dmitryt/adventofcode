import re
from utils import file

filepath = 'input/9.txt'

def exec():
  result = []
  def processLine(line) -> None:
    nonlocal result

    level = [int(el) for el in re.split(r'\s+', line[:-1])]
    last_elements = []

    while True:
      # print(level)
      is_all_zeros = True
      l = len(level)
      for i in range(1, l):
        el = level[i] - level[i - 1]
        if el != 0:
          is_all_zeros = False
        level.append(el)
      # append last el from previous level
      last_elements.append(level[l - 1])
      # remove elemenets from previous level
      level = level[l:]
      if is_all_zeros:
        break

    result.append(sum(last_elements))

  file.processFileLine(filepath, processLine)
  print("Result:", result, sum(result))

exec()