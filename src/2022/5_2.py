import re

filepath = 'input/5.txt'

def process_structure(line, rows):
  def update_rows(item, idx):
    if len(rows) <= idx:
      rows.append([])
    if item != '':
      rows[idx].insert(0, item)
    return idx + 1
  spaces = 1
  idx = 0
  for item in line.split(" "):
    if item == '':
      if (spaces % 4 == 0):
        idx = update_rows('', idx)
      spaces += 1
    else:
      idx = update_rows(item, idx)

def process_operations(line, rows):
  print(line)
  [amount, start, end] = re.match("move (\d+) from (\d+) to (\d+)", line).groups()
  start_row = rows[int(start) - 1]
  end_row = rows[int(end) - 1]
  i_amount = int(amount)
  # move items to the end row
  end_row.extend(start_row[len(start_row)-i_amount:])
  # remove items from the start row
  rows[int(start) - 1] = rows[int(start) - 1][:-i_amount]

def exec():
  is_map_inited = False
  rows = []
  with open(filepath, encoding="utf-8") as f:
    for line in f.readlines():
      ln = line[:-1]
      if ln == '':
        is_map_inited = True
        continue
      if is_map_inited is False:
        process_structure(ln, rows)
        continue
      process_operations(ln, rows)

    result = ''
    for item in rows:
      result += item[len(item) - 1]
    print(result)

exec()