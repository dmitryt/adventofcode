import re
import functools

filepath = 'input/15.txt'

item_re = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"

def find_distance(point1, point2):
  return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def compare(interval1, interval2):
  if interval2[0] > interval1[0]:
    return 1
  if interval2[0] < interval1[0]:
    return -1
  return 0

def exec():
  with open(filepath, encoding="utf-8") as f:
    content = f.read()
    sensors = []
    for matched in re.findall(item_re, content, re.MULTILINE):
      sensor = (int(matched[0]), int(matched[1]))
      beacon = (int(matched[2]), int(matched[3]))

      sensors.append((sensor[0], sensor[1], find_distance(sensor, beacon)))
    max_value = 4000000
    for y in range(max_value):
      if y % 100000 == 0:
        print("Processing y:", y)
      merged = []
      intervals = []
      for sensor in sensors:
        delta = sensor[2] - (y - sensor[1] if sensor[1] < y else sensor[1] - y)
        interval = (sensor[0] - delta, sensor[0] + delta)
        if interval[0] <= interval[1]:
          intervals.append(interval)
      intervals = sorted(intervals, key=functools.cmp_to_key(compare), reverse=True)
      for interval in intervals:
        if len(merged) == 0 or interval[0] > merged[-1][1] + 1:
          merged.append(list(interval))
        elif interval[0] <= merged[-1][1] + 1:
          merged[-1][1] = max(merged[-1][1], interval[1])
      if len(merged) > 1:
        print(y, merged)
        print("Result:", (merged[0][1] + 1) * 4000000 + y)
exec()