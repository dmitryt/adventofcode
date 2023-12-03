filepath = 'input/10.txt'

def exec():
  with open(filepath, encoding="utf-8") as f:
    x = 1
    total_ticks = 0
    result = 0
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
        total_ticks += 1
        if (total_ticks - 20) % 40 == 0:
          # print("Strength:", total_ticks, x * total_ticks)
          result += x * total_ticks
          # print(total_ticks, x)
      x += inc
    print("Result:", result)
exec()