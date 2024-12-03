
import numpy as np

def numerical_gradient_scalar(f:float, x:float):
  h = 1e-4 # 0.0001

  fxh1 = f(x-h)
  fxh2 = f(x+h)

  grad = (fxh2 - fxh1) / (2*h)
  return grad

def func01(x):
  return x*x+1.0

if __name__=="__main__":
  dydx = numerical_gradient_scalar(func01, 1.0)
  print(dydx)