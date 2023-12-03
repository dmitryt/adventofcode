import re

filepath = 'input/19_test.txt'

item_head_re = r"Blueprint (\d+):"
item_cost_re = r"Each (\w+) robot costs ([^.]+)."

class Blueprint:
  def __init__(self, idx, costs):
    self.idx = idx
    self.costs = costs
    self.actions = self.build_robot_actions()

  def build_robot_actions(self):
    actions = []
    for key, resources in self.costs.items():
      actions.append({ "type": key, "resources": resources })
    return actions

  def produce_states(self, state):
    result = []
    for action in self.actions:
      if self.can_apply_action(action, state):
        new_state = state.copy()
        for res, cnt in action["resources"].items():
          new_state["resources"][res] -= cnt
        result.append(new_state)
    return result

  def can_apply_action(self, action, state):
    return all(state["resources"][res] >= cnt for res, cnt in action["resources"].items())

def prepare_empty_state():
  state = { "resources": {}, "robots": {}, "timer": 0 }
  minerals = ["ore", "clay", "obsidian", "geode"]
  for m in minerals:
    state["resources"][m] = 0
    state["robots"][m] = 0
  state["robots"]["ore"] = 1
  return state

empty_state = prepare_empty_state()

def init():
  result = []
  with open(filepath, encoding="utf-8") as f:
    for line in f.readlines():
      ln = line[:-1]
      if ln == '':
        continue
      idx = int(re.match(item_head_re, ln)[1])
      costs = {}
      for matched in re.findall(item_cost_re, ln):
        cost = {}
        for m in matched[1].split('and'):
          amount, res = m.strip().split(' ')
          cost[res] = int(amount)
        costs[matched[0]] = cost
      result.append(Blueprint(idx, costs))
  return result

def exec():
  max_time = 1
  for blueprint in init():
    timer = 0
    queue = [empty_state.copy()]
    while timer < max_time:
      while True:
        if queue[0]["timer"] > timer:
          break
        state = queue.pop(0)
        states = blueprint.produce_states(state)
        print(states)
        break
      timer += 1
exec()