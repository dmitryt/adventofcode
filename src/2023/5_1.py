import re
import math
from utils import file, array

filepath = 'input/5.txt'

class Seed:
  def __init__(self, value) -> None:
    self.value = value
    self.storage = {}

  def set_property(self, key: str, value: int) -> None:
    self.storage[key] = value

  def get_property(self, key: str) -> int:
    return self.storage[key]

  def __repr__(self) -> str:
    return "Seed: " + str(self.value) + " " + str(self.storage)

class Mapper:
  @classmethod
  def build(self, block: str) -> 'Mapper':
    title, *ranges = block.split('\n')
    ranges = [array.to_int(re.split(r'\s+', r)) for r in ranges]
    source, target = re.findall(r'(\w+)-to-(\w+) map:', title)[0]
    return Mapper(source, target, ranges)

  def __init__(self, source: str, target: str, ranges: list) -> None:
    ranges.sort(key=lambda x: x[1])
    self.source = source
    self.target = target
    self.ranges = ranges

  def get_target_value(self, value: int) -> int:
    for r in self.ranges:
      if value >= r[1] and value < r[1] + r[2]:
        return r[0] + value - r[1]
    return value

  def __repr__(self) -> str:
    return "Mapper: " + self.source + "->" + self.target + " " + str(self.ranges)

def exec():
  seed_inputs, *blocks = file.read(filepath).split('\n\n')
  seed_inputs = [int(s) for s in re.split(r'\s+', seed_inputs.replace("seeds: ", ""))]
  seeds = []
  maps = {}
  for block in blocks:
    mapper = Mapper.build(block)
    maps[mapper.source] = mapper
  for value in seed_inputs:
    seed = Seed(value)
    mapper = maps['seed']
    value = seed.value
    while mapper is not None:
      value = mapper.get_target_value(value)
      seed.set_property(mapper.target, value)
      mapper = maps[mapper.target] if mapper.target in maps else None
    seeds.append(seed)
  seeds.sort(key=lambda x: x.get_property('location'))
  print("Result:", seeds[0])

exec()