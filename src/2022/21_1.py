filepath = 'input/21.txt'

def init():
  structure = {}
  with open(filepath, encoding="utf-8") as f:
    for line in f.readlines():
      (key, value) = line[:-1].split(': ')
      structure[key] = value
  return structure

def exec():
  def walk(node):
    if structure[node].isnumeric():
      return int(structure[node])
    child1, operation, child2 = structure[node].split(' ')
    fn = {
      '+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y,
    }[operation]
    return fn(walk(child1), walk(child2))

  structure = init()
  print(walk('root'))
exec()