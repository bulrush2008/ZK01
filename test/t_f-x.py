
import numpy as np

def f(x):
  # x is scalar or numpy array
  return x * 2.0

x = 1.0
y0 = f(x); print(y0, type(y0))

x = np.array([1.0, 2.0, 3.0])
y1 = f(x); print(y1, type(y1))

