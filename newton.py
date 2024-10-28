import matplotlib.pyplot as plt
import numpy as np

def dxf1(x):
	return 3 * (x[0] ** 2) - 3 * (x[1] ** 2)

def dyf1(x):
	return 6 * x[0]

def dxf2(x):
	return 6 * x[0]

def dyf2(x):
	return 3 * (x[1] ** 2)

def f1(x):
	return x[0]**3 - 3 * x[0] * (x[1] ** 2) -1

def f2(x):
	return 3 * (x[0] ** 2) - x[1] ** 3



A = np.ones((2, 2))
x = np.ones(2)
s = np.ones(2)

iteracao = 20
for i in range(iteracao):
	A[0][0] = dxf1(x)
	A[0][1] = dxf2(x)
	A[1][0] = dyf1(x)
	A[1][1] = dyf2(x)

	b = np.zeros(2)
	b[0] = f1(x)
	b[1] = f2(x)

	s = np.linalg.solve(A, -b)
	x[0] += s[0]
	x[1] += s[1]
	print(x)

print(x)
print(f1(x), f2(x))