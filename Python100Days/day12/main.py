point = 10

def increment_point():
  global point
  point = point + 1
  return point

print(increment_point())