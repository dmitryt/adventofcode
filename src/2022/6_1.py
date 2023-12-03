filepath = 'input/6.txt'

def exec():
  with open(filepath, encoding="utf-8") as f:
    result = 0
    win_length = 14
    win = {}
    line = f.readline()
    for idx in range(0, len(line)):
      char = line[idx]
      if char not in win:
        win[char] = 0
      win[char] += 1
      out_win_char_idx = idx - win_length
      if out_win_char_idx >= 0:
        out_win_char = line[out_win_char_idx]
        win[out_win_char] -= 1
        if win[out_win_char] == 0:
          del win[out_win_char]
      if len(win.keys()) == win_length:
        result = idx + 1
        break
    print("Result:", result)

exec()