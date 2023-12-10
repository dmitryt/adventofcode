import re
from utils import file
from functools import cmp_to_key, reduce

filepath = 'input/7.txt'

CARDS = (
  'J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'
)

CARDS_STORAGE = {}
for idx, card in enumerate(CARDS):
  CARDS_STORAGE[card] = idx

class CardsSet:
  def __init__(self, cards, bid) -> None:
    self.cards = cards
    self.bid = int(bid)
    self.rank = self.get_rank()

  def get_rank(self):
    store = {'A': 0}
    result = 0
    max_card = ('A', 0)
    for c in self.cards:
      if c not in store:
        store[c] = 0
      store[c] += 1
      if store[c] >= max_card[1] and c != 'J':
        max_card = (c, store[c])
    if 'J' in store:
      store[max_card[0]] += store['J']
      del store['J']
    for _, amount in store.items():
      if amount > 1:
        result += 10 ** (amount - 1)
    return result

  def __repr__(self) -> str:
    return "CardsSet: " + self.cards + " " + str(self.rank)

def compare_cards_sets(c1: CardsSet, c2: CardsSet) -> int:
  diff = c1.rank - c2.rank
  if diff != 0:
    return diff
  for idx, c in enumerate(c1.cards):
    if c == c2.cards[idx]:
      continue
    return CARDS_STORAGE[c] - CARDS_STORAGE[c2.cards[idx]]
  return 0

def exec():
  cardsSets = []

  def processLine(line) -> None:
    nonlocal cardsSets

    cards, bid = re.split(r'\s+', line)[:2]
    cardsSets.append(CardsSet(cards, bid))

  file.processFileLine(filepath, processLine)

  sorted_cards = sorted(cardsSets, key=cmp_to_key(compare_cards_sets))
  result = sum([ c.bid * (idx + 1) for idx, c in enumerate(sorted_cards)])
  print("Result:", result)

exec()