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

  def get_minimum_required_set(self):
    result = {}
    for gset in self.sets:
      for cube, amount in gset.cubes.items():
        if cube in result:
          result[cube] = max(amount, result[cube])
        else:
          result[cube] = amount
    return result

def exec():
  result = 0
  min_sets = []
  def processLine(line) -> None:
    min_sets.append(Game.build(line[:-1]).get_minimum_required_set())

  file.processFileLine(filepath, processLine)

  result = 0
  for min_set in min_sets:
    set_result = 1
    for _, amount in min_set.items():
      set_result *= amount
    result += set_result
  print(min_sets)
  print("Result:", result)
  # print([game.index for game in games])
  # print(sum(game.index for game in games))

exec()