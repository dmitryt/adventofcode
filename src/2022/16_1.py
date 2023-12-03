import re

filepath = 'input/16.txt'

item_re = r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)"

class Valve:
  def __init__(self, name, rate, siblings):
    self.name = name
    self.rate = rate
    self.siblings = siblings

  def __str__(self) -> str:
    return f'{self.name}, {self.rate}, {", ".join(self.siblings)}'

def init():
  with open(filepath, encoding="utf-8") as f:
    content = f.read()
    valves = {}
    first_valve = None
    for matched in re.findall(item_re, content, re.MULTILINE):
      if first_valve is None:
        first_valve = matched[0]
      valves[matched[0]] = Valve(matched[0], int(matched[1]), matched[2].split(', '))
    return valves, first_valve

def exec():
  def append(item, props):
    new_item = item.copy()
    new_item.update(props)
    queue.append(new_item)
    return new_item
  valves, first_valve = init()
  queue = [{"type": "move", "valve": first_valve, "total": 0, "delta": 0, "time": 0, "opened": set()}]
  max_time = 4
  max_total = 0
  while True:
    item = queue.pop(0)
    if item["time"] >= max_time:
      queue.insert(0, item)
      break
    valve = valves[item["valve"]]
    if item["type"] == "move" and valve.rate > 0 and valve.name not in item["opened"]:
      new_item = append(item, {"type": "open", "time": item["time"] + 1})
      new_item["opened"].add(valve.name)
    if item["type"] == "open":
      item["delta"] += valve.rate

    item["total"] += item["delta"]

    if item["total"] > max_total:
      max_total = item["total"]

    for sibling in valve.siblings:
      append(item, {"type": "move", "valve": sibling, "time": item["time"] + 1})
  print(len(queue), max_total)
exec()