import os
import functools

filepath = 'input/3.txt'

# ASCII Codes
# 'A-Z' => '65-90'
# 'a-z' => '97-122'

amount_of_letters = 26
lower_shift = 96
upper_shift = 64 - amount_of_letters

def process_item(item):
  print(item)
  if (item.isupper()):
    return ord(item) - upper_shift
  if (item.islower()):
    return ord(item) - lower_shift
  return ord(item)

def exec():
  with open(filepath, encoding="utf-8") as f:
    result = 0
    cnt = 0
    group = []
    common = []
    for line in f.readlines():
      cnt += 1
      group.append(set(list(line[:-1])))
      if cnt % 3 == 0:
        common_letter = functools.reduce(lambda x, y: x.intersection(y), group).pop()
        if common_letter is not None:
          common.append(common_letter)
        group = []

    common_ints = list(map(lambda x: process_item(x), common))
    print(common_ints)
    print("Result:", functools.reduce(lambda x, y: x + y, common_ints))

exec()