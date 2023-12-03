from utils import file

filepath = 'input/2.txt'

class GameSet:
  @classmethod
  def build(self, input: str) -> 'GameSet':
    gset = GameSet()
    for part in input.split(", "):
      cnt, cube_type = part.split(" ")
      gset.cubes[cube_type] = int(cnt)
    return gset

  def check(self, requirement: 'GameSet') -> bool:
    for cube, amount in self.cubes.items():
      if cube not in requirement.cubes or requirement.cubes[cube] < amount:
        return False
    return True

  def __init__(self) -> None:
    self.cubes = {}

  def __repr__(self) -> str:
    return "Set " + str(self.cubes)

class Game:
  @classmethod
  def build(self, input: str) -> 'Game':
    title, rest = input.split(": ")
    game = Game(int(title.split(" ")[1]))
    game.build_sets(rest)
    return game

  def __init__(self, index: int) -> None:
    self.index = index
    self.sets = []

  def __repr__(self) -> str:
    return "Game " + str(self.index) + " sets: " + str(self.sets)

  def build_sets(self, input: str) -> None:
    self.sets = [GameSet.build(part) for part in input.split("; ")]

  def is_possible(self, requirement: GameSet) -> bool:
    for gset in self.sets:
      if gset.check(requirement) is False:
        return False
    return True

def exec():
  games = []
  required_set = GameSet.build("12 red, 13 green, 14 blue")
  def processLine(line) -> None:
    # nonlocal games
    game = Game.build(line[:-1])
    if (game.is_possible(required_set)):
      games.append(game)

  file.processFileLine(filepath, processLine)
  print([game.index for game in games])
  print(sum(game.index for game in games))

exec()