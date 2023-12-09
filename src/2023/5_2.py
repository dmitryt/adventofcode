import re
import math
from utils import file, array

filepath = 'input/5_dev.txt'

class Seed:
  def __init__(self, range) -> None:
    self.range = range
    self.storage = {}

  def set_property(self, key: str, value: int) -> None:
    self.storage[key] = value

  def get_property(self, key: str) -> int:
    return self.storage[key]

  def __repr__(self) -> str:
    return "Seed: " + str(self.range) + " " + str(self.storage)

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

def generate_seed_ranges(input: str) -> list:
  result = []
  seed_inputs = [int(s) for s in re.split(r'\s+', input.replace("seeds: ", ""))]
  for index, value in enumerate(seed_inputs):
    if index % 2 != 0:
      result.append((seed_inputs[index - 1], value))
  return result


def exec():
  head, *blocks = file.read(filepath).split('\n\n')
  seeds = []
  maps = {}
  for block in blocks:
    mapper = Mapper.build(block)
    maps[mapper.source] = mapper
  for r in generate_seed_ranges(head):
    seed = Seed(r)
    mapper = maps['seed']
    ranges = [seed.range]
    while mapper is not None:
      ranges = mapper.get_target_ranges(ranges)
      seed.set_property(mapper.target, ranges)
      mapper = maps[mapper.target] if mapper.target in maps else None
    seeds.append(seed)
  # seeds.sort(key=lambda x: x.get_property('location'))
  # print("Result:", seeds[0])

exec()