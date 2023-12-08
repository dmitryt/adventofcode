import re
import math
from functools import reduce

from utils import file, array

filepath = 'input/6.txt'

class Races:
  def __init__(self, time: int, distance: int) -> None:
    self.time = time
    self.distance = distance

  def __repr__(self) -> str:
    return "Race: time:" + str(self.time) + ", distance:" + str(self.distance)

  def compare(self):
    result = []
    for speed in range(1, self.time):
      existing_time = self.time - speed
      distance = existing_time * speed
      if distance > self.distance:
        result.append((speed, distance))
    return result

def exec():
  times, distances = file.read(filepath).split('\n')
  times = [int(el) for el in re.split(r'\s+', times)[1:]]
  distances = [int(el) for el in re.split(r'\s+', distances)[1:]]
  result = []
  for idx, time in enumerate(times):
    races = Races(time, distances[idx])
    result.append(len(races.compare()))

  print("Result:", reduce(lambda x, y: x * y, result))

exec()