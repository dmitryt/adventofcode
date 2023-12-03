import os

filepath = 'input/1.txt'

def exec():
  with open(filepath, encoding="utf-8") as f:
    result = 0
    for line in f.readlines():
      line_result = False
      num = False
      for char in line:
        if char == "\n":
          continue
        if char.isdigit():
          num = int(char)
          if line_result is False:
            line_result = num * 10
      line_result += num
      result += line_result
    print("Result:", result)

exec()