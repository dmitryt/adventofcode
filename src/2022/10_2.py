filepath = 'input/10.txt'

def exec():
  with open(filepath, encoding="utf-8") as f:
    x = 1
    total_ticks = 0
    result = ''
    for line in f.readlines():
      args = line[:-1].split(' ')
      ticks = 0
      inc = 0
      if args[0] == 'noop':
        ticks = 1
      elif args[0] == 'addx':
        ticks = 2
        inc = int(args[1])
      for _ in range(ticks):
        result += '#' if abs(total_ticks - x) <= 1 else '.'
        total_ticks += 1
        if total_ticks % 40 == 0:
          total_ticks = 0
          result += '\n'
      x += inc
    print(result)
exec()