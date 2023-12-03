import os

filepath = 'input/4.txt'

def exec():
  def split_range(input):
    return list(map(lambda x: int(x), input.split('-')))
  with open(filepath, encoding="utf-8") as f:
    result = 0
    for line in f.readlines():
      ranges = list(map(split_range, line[:-1].split(',')))
      [first, second] = ranges
      is_overlap = first[1] >= second[0] if first[0] < second[0] else second[1] >= first[0]
      if is_overlap:
          result += 1
    print("Result:", result)

exec()