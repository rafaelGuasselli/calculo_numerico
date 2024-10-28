import numpy as np 
import matplotlib.pyplot as plt

def f(x):
	return  x**4 - 3*(x**3) + x**2 + x + 1

x = np.linspace(-3, 3, 100)
plt.plot(x, f(x), label="$f(x)$")
plt.ylim(-1, 1)
plt.grid()
plt.legend()
plt.show()