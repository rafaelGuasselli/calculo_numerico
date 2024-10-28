# import numpy as np 
# import matplotlib.pyplot as plt

n = int(input())
a = [-1] * n
c = [-1] * n
d = [2]  * n

b = [0] * n
b[n-1] = 50

m = [0] * (n+1) 
x = [0] * (n+1)

for i in range(0, n-1):
	m[i+1] = a[i+1]/d[i]
	d[i+1] = d[i+1] - m[i+1] * c[i] 
	b[i+1] = b[i+1] - m[i+1] * b[i]

x[n-1] = b[n-1]/d[n-1]
for i in range(n-2, -1, -1):
	x[i] = ((b[i]-c[i]*x[i+1])/d[i])

for i in range(0, n):
	print("{:.2f}".format(x[i])) 


# plt.plot(x, "b.", label="$T[i]$")
# plt.xlim(0, n-1)
# plt.grid()
# plt.legend()
# plt.show()