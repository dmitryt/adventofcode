def create_empty_matrix(rows: int, cols: int, default_value = None):
  return [[default_value for _ in range(cols)] for _ in range(rows)]
