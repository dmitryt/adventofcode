import re
from utils import file

filepath = 'input/9.txt'

def exec():
  result = []
  def processLine(line) -> None:
    nonlocal result

    level = [int(el) for el in re.split(r'\s+', line[:-1])]
    first_elements = []

    while True:
      # print(level)
      is_all_zeros = True
      l = len(level)
      for i in range(1, l):
        el = level[i] - level[i - 1]
        if el != 0:
          is_all_zeros = False
        level.append(el)
      # append first el from previous level
      first_elements.append(level[0])
      # remove elements from previous level
      level = level[l:]
      if is_all_zeros:
        break
    sub_result = first_elements[0]
    sign = -1

    for i in range(len(first_elements) - 1):
      sub_result += first_elements[i + 1] * sign
      sign *= -1

    result.append(sub_result)

  file.processFileLine(filepath, processLine)
  print("Result:", result, sum(result))

exec()