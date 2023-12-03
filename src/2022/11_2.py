import re
import math
import time

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
    def process_arg(arg):
      return 'old' if arg == 'old' else int(arg)

    self.items = items
    [arg1, operation, arg2] = operation.replace('new = ', '').split(' ')
    self.operation = [process_arg(arg1), operation, process_arg(arg2)]
    self.test = test
    self.total = 0

  def exec_operation(self, item):
    def process_arg(arg):
      return item if arg == 'old' else arg

    [arg1, operation, arg2] = self.operation
    if operation == '+':
      return process_arg(arg1) + process_arg(arg2)
    if operation == '*':
      return process_arg(arg1) * process_arg(arg2)

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
  cycles = 1000
  for cnt in range(cycles):
    print("CNT", cnt)
    for m in monkeys:
      m.total += len(m.items)
      # if cnt == cycles - 1:
      # print(m.total)
      for item in m.items:
        # if cnt > 600:
        print("p1")
        s1 = time.time()
        result = m.exec_operation(item)
        s2 = time.time()
        print("p2", s2-s1)
        item_to_push = result
        idx = m.test[1] if (item_to_push % m.test[0]) == 0 else m.test[2]
        s3 = time.time()
        print("p3", s3-s2)
        # print("Result", idx, item_to_push)
        monkeys[idx].items.append(item_to_push)
        s4 = time.time()
        print("p4", s4 - s3)
      m.items = []
  # for m in monkeys:
  #   print(str(m.items))
  #   print("====")
  # totals = sorted(list(map(lambda x: x.total, monkeys)), reverse=True)
  # print("Result:", totals[0] * totals[1])
exec()