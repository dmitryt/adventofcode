import functools
filepath = 'input/13.txt'

def process_item(line):
  result = None
  stack = [[]]
  el = None
  if line[0] != '[':
    # We suppose to compare arrays
    return []
  for char in line[1:]:
    if char == '[':
      stack.append([])
    elif char == ']' or char == ',':
      if el is not None:
        stack[-1].append(el)
        el = None
      if char == ']':
        item = stack.pop()
        if len(stack) == 0:
          result = item
        else:
          stack[-1].append(item)
    elif char.isnumeric():
      el = int(char) if el is None else el * 10 + int(char)
  return result

def init():
  result = []
  with open(filepath, encoding="utf-8") as f:
    for line in f.readlines():
      ln = line[:-1]
      if ln == '':
        continue
      result.append(process_item(ln))
  return result

def compare(list1, list2):
  def make_list(el):
    return el if type(el) is list else [el]
  for i in range(min(len(list1), len(list2))):
    result = 0
    if type(list1[i]) is list or type(list2[i]) is list:
      result = compare(make_list(list1[i]), make_list(list2[i]))
    else:
      if list2[i] > list1[i]:
        result = 1
      if list2[i] < list1[i]:
        result = -1
    if result == 0:
      continue
    else:
      return result
  if len(list2) > len(list1):
    return 1
  if len(list2) < len(list1):
    return -1
  return 0

def exec():
  arr = init()
  result = 1
  arr.extend([[[2]], [[6]]])
  sorted_list = sorted(arr, key=functools.cmp_to_key(compare), reverse=True)
  for i in range(len(sorted_list)):
    if str(sorted_list[i]) == '[[2]]' or str(sorted_list[i]) == '[[6]]':
      result *= (i + 1)
  print(result)
exec()