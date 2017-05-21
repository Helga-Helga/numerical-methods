from function import f

def runge_kutta(h, left, right):
  x, y = 0, 0
  result = []
  x_axis = []
  while right >= left:
      result.append(y)
      x_axis.append(x)
      left += h
      k1 = h * f(x, y)
      k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
      k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
      k4 = h * f(x + h, y + k3)
      y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
      x = left
  result.append(y)
  x_axis.append(x)
  return x_axis, result
