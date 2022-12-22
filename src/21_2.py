import functools

filepath = 'input/21.txt'

class TreeNode:
  def __init__(self, name) -> None:
    self.name = name

  def find(self, name, path = []):
    return path + [self.name] if self.name == name else None

  def calculate(self):
    pass

class Node(TreeNode):
  operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
  }
  opposit_operations = {
    '+': '-',
    '-': '+',
    '*': '/',
    '/': '*',
  }

  def __init__(self, name, children, operation) -> None:
    super().__init__(name)
    self.children = children
    self.operation = operation

  def find(self, name, path = []):
    result = super().find(name, path)
    if result is not None:
      return result
    children_result = list(map(lambda x: x.find(name, path + [self.name]), self.children))
    children_result = list(filter(lambda x: x is not None, children_result))
    return None if len(children_result) == 0 else children_result[0]

  def calculate(self):
    fn = self.operations[self.operation]
    calculations = list(map(lambda x: x.calculate(), self.children))
    return functools.reduce(fn, calculations)

  def decalculate(self, result_value, human_ancestor_idx):
    non_human_ancestor = self.children[(human_ancestor_idx + 1) % 2]
    non_human_value = non_human_ancestor.calculate()

    if result_value is None:
      return non_human_value

    fn = self.operations[self.operation]
    if self.operation == '+' or self.operation == '*' or human_ancestor_idx == 0:
      fn = self.operations[self.opposit_operations[self.operation]]
      return fn(result_value, non_human_value)

    return fn(non_human_value, result_value)

class Leaf(TreeNode):
  def __init__(self, name, value) -> None:
    super().__init__(name)
    self.value = value

  def calculate(self):
    return self.value

def process_structure():
  structure = {}
  with open(filepath, encoding="utf-8") as f:
    for line in f.readlines():
      (key, value) = line[:-1].split(': ')
      structure[key] = value
  return structure

def exec():
  def init_tree(name):
    if structure[name].isnumeric():
      return Leaf(name, int(structure[name]))
    child1, operation, child2 = structure[name].split(' ')
    return Node(name, [init_tree(child1), init_tree(child2)], operation)

  def walk(node, value):
    # print(node.name, value)
    if isinstance(node, Leaf):
      return value if node.name in human_path else node.calculate()
    human_ancestor_idx = [index for (index, item) in enumerate(node.children) if item.name in human_path][0]
    human_ancestor = node.children[human_ancestor_idx]
    return walk(human_ancestor, node.decalculate(value, human_ancestor_idx))


  human_node = 'humn'
  structure = process_structure()
  rootNode = init_tree('root')
  human_path = set(rootNode.find(human_node))
  print("Result:", walk(rootNode, None))
exec()