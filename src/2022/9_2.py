filepath = 'input/9.txt'

DIRECTIONS = {
  'R': (0, 1),
  'L': (0, -1),
  'U': (1, 0),
  'D': (-1, 0),
}

def adjust_knot(head_coords, tail_coords):
  [x_head, y_head] = head_coords
  [x_tail, y_tail] = tail_coords
  dx = x_head - x_tail
  dy = y_head - y_tail
  if abs(dx) <= 1 and abs(dy) <= 1:
    return [x_tail, y_tail]
  x_tail += dx + (-1 if dx > 0 else 1)
  y_tail += dy + (-1 if dy > 0 else 1)
  if abs(dx) < 2:
    x_tail = x_head
  elif abs(dy) < 2:
    y_tail = y_head
  return [x_tail, y_tail]

def make_step(base_coords, step):
  [i, j] = base_coords
  [di, dj] = step
  return [i + di, j + dj]

def exec():
  with open(filepath, encoding="utf-8") as f:
    rope = [[0,0] for _ in range(10)]
    positions = set()
    positions.add(str(rope[0]))
    for line in f.readlines():
      [direction, step] = line[:-1].split(' ')
      for i in range(int(step)):
        rope[0] = make_step(rope[0], DIRECTIONS[direction])
        for j in range(1, len(rope)):
          rope[j] = adjust_knot(rope[j - 1], rope[j])
        positions.add(str(rope[-1]))
    print(len(positions))
exec()