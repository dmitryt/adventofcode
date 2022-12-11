import functools

filepath = 'input/7.txt'

class TreeNode:
  def __init__(self, path, type, size = 0):
    self.parent = None
    self.path = path
    self.type = type
    self.size = size
    self.nodes = {}

  def addChild(self, node):
    node.parent = self
    self.size += node.size
    self.nodes[node.path] = node

  def getNode(self, path):
    return self.nodes[path] if path in self.nodes else None

  def recalculate_size(self):
    self.size = 0
    for key, node in self.nodes.items():
      self.size += node.size

  def collect_folders(self):
    result = []
    for key, node in self.nodes.items():
      if node.type == 'folder':
        result.append((node.path, node.size))
    return result

def process_command(line, folder, folders):
  line_arr = line[2:].split(' ')
  cmd = line_arr[0]
  if cmd == 'cd':
    path = line_arr[1]
    if path == '..':
      folders.extend(folder.collect_folders())
      folder.recalculate_size()
      folder = folder.parent
    else:
      node = folder.getNode(path)
      if node is not None and node.type == 'folder':
        folder = node
  if cmd == 'ls' or cmd == 'cd':
    return cmd, folder
  raise ValueError('Unsupported command', cmd)

def process_structure(line, folder):
  line_arr = line.split(' ')
  if line_arr[0] == 'dir':
    folder.addChild(TreeNode(line_arr[1], 'folder'))
  else:
    folder.addChild(TreeNode(line_arr[1], 'file', int(line_arr[0])))


def exec():
  with open(filepath, encoding="utf-8") as f:
    folder = TreeNode(None, None, 0)
    folder.addChild(TreeNode('/', 'folder'))
    cmd = None
    folders = []
    for line in f.readlines():
      ln = line[:-1]
      if ln.startswith('$'):
        cmd, folder = process_command(ln, folder, folders)
      elif cmd == 'ls':
        process_structure(ln, folder)
    # coming back to the root to recalculate the size for all subfolders
    while folder is not None:
      _, folder = process_command('$ cd ..', folder, folders)
    folders.sort(key=lambda item: item[1], reverse=True)
    root = folders[0]
    total_space = 70000000
    required_space = 30000000
    free_space = total_space - root[1]
    prev_item = None
    for item in folders[1:]:
      if free_space + item[1] < required_space:
        print("Result", prev_item)
        break
      prev_item = item

exec()