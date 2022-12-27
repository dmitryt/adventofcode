filepath = 'input/25.txt'

def dec_2_snafu(dec):
  result = ""
  next_reg = 0
  while dec != 0:
    mod = dec % 5
    if mod <= 2:
      next_reg = 0
      result = str(mod) + result
    else:
      next_reg = 1
      result = ("=" if mod == 3 else "-") + result
    dec -= mod
    if dec == 0:
      break
    if dec % 5 == 0:
      dec = int(dec / 5) + next_reg
  return result if next_reg == 0 else str(next_reg) + result

def snafu_2_dec(snafu):
  def get_int(char):
    if char == '-':
      return -1
    if char == '=':
      return -2
    return int(char)
  result = 0
  for idx in range(len(snafu)):
    result += (5 ** idx) * get_int(snafu[ - idx - 1])
  return result


def exec():
  with open(filepath, encoding="utf-8") as f:
    sum = 0
    for line in f.readlines():
      sum += snafu_2_dec(line[:-1])
    print("Result:", dec_2_snafu(sum))
  # print("3 =>", dec_2_snafu(3))
  # print("7 =>", dec_2_snafu(7))
  # print("107 =>", dec_2_snafu(107))
  # print("353 =>", dec_2_snafu(353))
  # print("32 =>", dec_2_snafu(32))
  # print("1257 =>", dec_2_snafu(1257))
  # print("31 =>", dec_2_snafu(31))
  # print("201 =>", dec_2_snafu(201))
  # print("11 =>", dec_2_snafu(11))
  # print("198 =>", dec_2_snafu(198))
  # print("906 =>", dec_2_snafu(906))
  # print("1747 =>", dec_2_snafu(1747))
exec()