class TrieNode:
  def __init__(self, value = None) -> None:
    self.value = value
    self.storage = {}

  def insert[T](self, word: str, value: T) -> None:
    if word == "":
      return
    char = word[0]
    if char not in self.storage:
      self.storage[char] = TrieNode(value)

    self.storage[char].insert(word[1:], value)

  def is_token(self) -> bool:
    return len(self.storage.keys()) == 0

  def get(self, char: str) -> 'TrieNode':
    return self.storage[char] if char in self.storage else None

  def has(self, word: str) -> bool:
    if len(word) == 0 or word[0] not in self.storage:
      return False
    elif len(word) == 1:
      return self.storage[word[0]].is_empty()
    return self.storage[word[0]].search(word[1:])

  def __str__(self) -> str:
    result = 'TrieNode, value: ' + str(self.value) + ' storage: {'
    for key, value in self.storage.items():
      result += key + ": " + str(value)
    return result + "}"