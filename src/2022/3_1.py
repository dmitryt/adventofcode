import os

filepath = 'input/3.txt'

# ASCII Codes
# 'A-Z' => '65-90'
# 'a-z' => '97-122'

amount_of_letters = 26
lower_shift = 96
upper_shift = 64 - amount_of_letters

def process_item(item):
  if (item.isupper()):
    return ord(item) - upper_shift
  if (item.islower()):
    return ord(item) - lower_shift
  return ord(item)

def exec():
  with open(filepath, encoding="utf-8") as f:
    result = 0
    for line in f.readlines():
      half = int(len(line) / 2)
      line = ''.join(sorted(line[:half])) + ''.join(sorted(line[half:-1]))
      i = j = 0
      while i < half and j < half:
        if line[i] < line[half + j]:
          i += 1
        elif line[half + j] < line[i]:
          j += 1
        else:
          break
      # print("Found common item:", line[i], process_item(line[i]))
      result += process_item(line[i])
    print("Result:", result)

exec()