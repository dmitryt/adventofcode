filepath = 'input/20.txt'

def init():
  arr = []
  with open(filepath, encoding="utf-8") as f:
    for line in f.readlines():
      ln = line[:-1]
      if ln == '':
        continue
      arr.append(int(ln))
  return arr

def exec():
  def move_el(el):
    idx = [index for index, item in enumerate(arr) if item == el][0]
    arr.pop(idx)
    arr.insert((idx + el) % len(arr), el)
  orig_arr = init()
  arr = orig_arr.copy()
  for idx in range(len(orig_arr)):
    move_el(orig_arr[idx])
    # print(arr)
  zero_idx = [index for index, item in enumerate(arr) if item == 0][0]
  print(arr)
  print(zero_idx)
  print("1000th item:", arr[(zero_idx + 1000) % len(arr)])
  print("2000th item:", arr[(zero_idx + 2000) % len(arr)])
  print("3000th item:", arr[(zero_idx + 3000) % len(arr)])
  print("Result:", arr[(zero_idx + 1000) % len(arr)] + arr[(zero_idx + 2000) % len(arr)] + arr[(zero_idx + 3000) % len(arr)])
exec()