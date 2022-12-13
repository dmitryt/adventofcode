filepath = 'input/9.txt'

DIRECTIONS = {
  'R': (0, 1),
  'L': (0, -1),
  'U': (1, 0),
  'D': (-1, 0),
}

def adjust_tail(head_coords, tail_coords):
  [x_head, y_head] = head_coords
  [x_tail, y_tail] = tail_coords
  dx = x_head - x_tail
  dy = y_head - y_tail
  if abs(dx) == 2:
    x_tail += dx + (-1 if dx > 0 else 1)
    y_tail = y_head
  if abs(dy) == 2:
    x_tail = x_head
    y_tail += dy + (-1 if dy > 0 else 1)
  return [x_tail, y_tail]

def make_step(base_coords, step):
  [i, j] = base_coords
  [di, dj] = step
  return [i + di, j + dj]

def exec():
  with open(filepath, encoding="utf-8") as f:
    head_coords = [0,0]
    tail_coords = [0,0]
    positions = set()
    positions.add(str(tail_coords))
    for line in f.readlines():
      [direction, step] = line[:-1].split(' ')
      for i in range(0, int(step)):
        head_coords = make_step(head_coords, DIRECTIONS[direction])
        tail_coords = adjust_tail(head_coords, tail_coords)
        positions.add(str(tail_coords))
        # print("Head", head_coords, "Tail:", tail_coords)
    print(len(positions))
exec()