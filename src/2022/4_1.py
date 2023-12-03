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
      is_first_contains_second = first[0] <= second[0] and first[1] >= second[1];
      is_second_contains_first = second[0] <= first[0] and second[1] >= first[1];
      if is_first_contains_second or is_second_contains_first:
        result += 1
    print("Result:", result)

exec()