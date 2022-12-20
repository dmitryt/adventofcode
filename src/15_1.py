import re

filepath = 'input/15.txt'

item_re = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"

def exec():
  with open(filepath, encoding="utf-8") as f:
    content = f.read()
    y = 2000000
    result_set = set()
    beacons = []
    for matched in re.findall(item_re, content, re.MULTILINE):
      sensor = (int(matched[0]), int(matched[1]))
      beacon = (int(matched[2]), int(matched[3]))
      beacons.append(beacon)

      distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
      delta = distance - (y - sensor[1] if sensor[1] < y else sensor[1] - y)
      section = list(range(sensor[0] - delta, sensor[0] + delta + 1))
      result_set.update(section)
      print(sensor, beacon)
    for beacon in beacons:
      if beacon[1] == y and beacon[0] in result_set:
        result_set.remove(beacon[0])
  print(len(result_set))
exec()