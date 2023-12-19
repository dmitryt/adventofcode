import re
from pprint import pprint
from utils import file

filepath = 'input/15.txt'

def get_hash(seq: str) -> int:
  result = 0
  for char in seq:
    print(char, ord(char), result)
    result += ord(char)
    result *= 17
    result = result % 256

  return result

def exec():
  result = 0
  for expr in file.read(filepath).split(','):
    result += get_hash(expr)
  print("Result:", result)

exec()