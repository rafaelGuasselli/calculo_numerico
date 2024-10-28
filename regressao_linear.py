import matplotlib.pyplot as plt
import numpy as np

def g(x, a):
	y = a[0] * x + a[1] * np.cos(x)
	return y

def residuo(a, x, y):
	return g(x, a) - y

xi = np.array([0, 1.5, 3, 4.5, 6])
yi = np.array([1, 1.57, 2, 4.3, 7])

n = len(xi)
v1 = np.ones(n)
A = np.zeros((2, 2))

A[0][0] = np.vdot(xi, xi)
A[0][1] = np.vdot(np.cos(xi), xi)
A[1][0] = np.vdot(np.cos(xi), xi)
A[1][1] = np.vdot(np.cos(xi), np.cos(xi))

b = np.zeros(2)
b[0] = np.vdot(xi, yi)
b[1] = np.vdot(np.cos(xi), yi)

print(A, b)
a = np.linalg.solve(A, b)
print(a)

res = 0
for i in range(n):
	res += residuo(a, xi[i], yi[i]) ** 2

print(res)

x = np.linspace(xi[0], xi[n-1], 100)
y = g(x, a)


plt.figure(1)
plt.plot(xi, yi, 'o', label = '$y_i$')
plt.plot(x, y, label = "$g(x)$")
plt.show()
