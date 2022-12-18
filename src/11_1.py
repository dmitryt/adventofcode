import re
import math

filepath = 'input/11.txt'

monkey_re = r"""Monkey \d+:
  Starting items: (?P<items>.*)
  Operation: (?P<operation>.*)
  Test: divisible by (?P<divisible_by>\d+)
    If true: throw to monkey (?P<success_monkey>\d+)
    If false: throw to monkey (?P<failure_monkey>\d+)
"""

class Monkey:
  def __init__(self, items, operation, test):
    self.items = items
    self.operation = operation.replace('new = ', '')
    self.test = test
    self.total = 0

  def exec_operation(self, item):
    def process_arg(arg):
      return item if arg == 'old' else int(arg)

    [arg1, operation, arg2] = self.operation.split(' ')
    arg1 = process_arg(arg1)
    arg2 = process_arg(arg2)
    if operation == '+':
      return arg1 + arg2
    if operation == '*':
      return arg1 * arg2

def init():
  collections = []
  with open(filepath, encoding="utf-8") as f:
    content = f.read()
    for matched in re.findall(monkey_re, content, re.MULTILINE):
      [items, operation, divisible_by, success_monkey, failure_monkey] = matched
      test = list(map(
        lambda x: int(x),
        [divisible_by, success_monkey, failure_monkey]
      ))
      monkey = Monkey(
        list(map(lambda x: int(x), items.split(', '))),
        operation,
        test
      )
      collections.append(monkey)
  return collections

def exec():
  monkeys = init()
  cycles = 20
  for _ in range(cycles):
    for m in monkeys:
      m.total += len(m.items)
      for item in m.items:
        result = m.exec_operation(item)
        item_to_push = math.floor(result / 3)
        idx = m.test[1] if (item_to_push % m.test[0]) == 0 else m.test[2]
        # print("Result", idx, item_to_push)
        monkeys[idx].items.append(item_to_push)
      m.items = []
  totals = sorted(list(map(lambda x: x.total, monkeys)), reverse=True)
  print("Result:", totals[0] * totals[1])
exec()