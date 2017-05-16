def newton_interpolation(x, y, u):
  '''
  Parameters
  ----------
  x : list of floats
  y : list of floats
  u : float

  Returns
  -------
  float
      an estimate at the point u
  '''
  g = y[:]
  s = g[0]
  for i in range(len(y)-1):
    g = [(g[j+1]-g[j])/(x[j+i+1]-x[j]) for j in range(len(g)-1)]
    s += g[0] * product(u-x[j] for j in range(i+1))
  return s

def product(a):
  p = 1
  for i in a: p *= i
  return p
