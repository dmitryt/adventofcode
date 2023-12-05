import re
from utils import file

filepath = 'input/4.txt'

def split_numbers(line: str) -> tuple:
  parts = re.sub(r'Card\s+\d+: ', '', line).split(' | ')
  return [re.split(r'\s+', part.strip()) for part in parts]

def exec():
  games = []
  game_idx = 0

  def processLine(line) -> None:
    nonlocal games, game_idx
    winning_numbers, numbers = split_numbers(line)
    winning_numbers_dict = {}
    if len(games) == game_idx:
      games.append(1)
    for num in winning_numbers:
      winning_numbers_dict[num] = True
    wins = 0
    for num in numbers:
      if num in winning_numbers_dict:
        wins += 1
    if wins > 0:
        for i in range(game_idx + 1, game_idx + wins + 1):
          if len(games) == i:
            games.append(1)
          games[i] += games[game_idx]
    game_idx += 1
    # print(games)

  file.processFileLine(filepath, processLine)
  print("Result:", sum(games))

exec()