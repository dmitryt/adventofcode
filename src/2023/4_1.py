import re
from utils import file

filepath = 'input/4.txt'

def split_numbers(line: str) -> tuple:
  parts = re.sub(r'Card\s+\d+: ', '', line).split(' | ')
  return [re.split(r'\s+', part.strip()) for part in parts]

def exec():
  result = 0

  def processLine(line) -> None:
    nonlocal result
    line_result = 0
    winning_numbers, numbers = split_numbers(line)
    winning_numbers_dict = {}
    for num in winning_numbers:
      winning_numbers_dict[num] = True
    for num in numbers:
      if num in winning_numbers_dict:
        line_result = 1 if line_result == 0 else line_result * 2
    print(line_result)
    result += line_result

  file.processFileLine(filepath, processLine)
  print("Result:", result)

exec()