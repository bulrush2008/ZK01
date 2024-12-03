
import numpy as np

def numerical_gradient_vec(f:np.ndarray, x:np.ndarray):
  h = 1e-4 # 0.0001

  grad = np.zeros_like(x)

  for idx in range(x.size):
    tv = x[idx] - h
    fb = f(tv)

    tv = x[idx] + h
    ff = f(tv)

    grad[idx] = (ff - fb) / (2.0*h)

  return grad

def func01(x):
  return x*x+1.0

if __name__=="__main__":
  dydx = numerical_gradient_vec(func01, np.array([1.0]))
  print(dydx)