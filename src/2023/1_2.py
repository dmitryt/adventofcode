import os
from utils import trie
from utils import file

filepath = 'input/1.txt'

root_trie = trie.TrieNode()
numbers = (
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
)
for index, word in enumerate(numbers):
  root_trie.insert(word, index + 1)

def get_trie_or_reset(trie: trie.TrieNode, char: str) -> trie.TrieNode:
  new_trie = trie.get(char)
  if new_trie is None:
    return root_trie.get(char) or root_trie
  return new_trie

def exec():
  result = 0

  def processLine(line) -> None:
    nonlocal result
    numbers = []
    trie = root_trie

    for char in line:
      if char == "\n":
        continue
      trie = get_trie_or_reset(trie, char)

      if char.isdigit():
        numbers.append(int(char))

      if trie and trie.is_token():
        numbers.append(trie.value)
        trie = get_trie_or_reset(trie, char)

    result += numbers[0] * 10 + numbers[-1]
    print(line[0:-1], numbers[0] * 10 + numbers[-1], result)

  file.processFileLine(filepath, processLine)
  print("Result:", result)

exec()