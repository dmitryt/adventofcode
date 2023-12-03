def processFileLine(filepath: str, cb) -> None:
  with open(filepath, encoding="utf-8") as f:
    for line in f.readlines():
      cb(line)