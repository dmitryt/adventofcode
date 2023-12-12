def clean_empty_values(d: dict, empty_value = False) -> dict:
  return { key: value for key, value in d.items() if value != empty_value }
