import re
from pprint import pprint
from utils import file

filepath = 'input/15.txt'

def split_lens(lens: str) -> list:
  m = re.search(r'[-=]', lens)
  if m:
    index = m.start()
    return [lens[:index], lens[index], int(lens[index + 1]) if index < len(lens) - 1 else None]

  return [lens]


def get_hash(seq: str) -> int:
  result = 0
  for char in seq:
    result += ord(char)
    result *= 17
    result = result % 256

  return result

def delete_or_insert(lens: list, key: str, value: int, oper: str) -> bool:
  for idx, box in enumerate(lens):
    if box[0] == key:
      if oper == '-':
        del lens[idx]
      elif oper == '=':
        lens[idx][1] = value
      return True

  return False

def exec():
  result = 0
  boxes = {}
  for lens in file.read(filepath).split(','):
    label, oper, focal = split_lens(lens)
    box_index = get_hash(label)
    if box_index not in boxes:
      boxes[box_index] = []
    res = delete_or_insert(boxes[box_index], label, focal, oper)
    if res == False and oper == '=':
      boxes[box_index].append([label, focal])

  for box_idx, lenses in boxes.items():
    for i, lens in enumerate(lenses):
      result += (box_idx + 1) * (i + 1) * lens[1]
  print(boxes)
  print("Result:", result)

exec()