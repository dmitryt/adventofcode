def processFileLine(filepath: str, cb) -> None:
  with open(filepath, encoding="utf-8") as f:
    for line in f.readlines():
      cb(line)

def read(filepath: str) -> None:
  with open(filepath, encoding="utf-8") as f:
    return f.read()

def readIntoMatrix(filepath: str) -> list:
  result = []
  def process(line):
    nonlocal result
    result.append(list(line[:-1] if line[-1] == "\n" else line))

  processFileLine(filepath, process)
  return result