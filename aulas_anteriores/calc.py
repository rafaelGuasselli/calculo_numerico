import numpy as np

def calc(y, x, precision):
	result = 1
	for i in range(0, precision):
		frac = (pow(np.log(y), i) * (pow(x, i)))
		for j in range(2, i+1):
			frac /= j
		result += frac
	return result

 
x = 10
print(f"objetivo: {np.exp(x)}")
print(calc(np.exp(1), x, 1))
print(calc(np.exp(1), x, 2))
print(calc(np.exp(1), x, 10))
print(calc(np.exp(1), x, 100))
print(calc(np.exp(1), x, 200))

print("----------------------")
print(f"objetivo: {pow(2, x)}")
print(calc(2, x, 1))
print(calc(2, x, 2))
print(calc(2, x, 10))
print(calc(2, x, 100))
print(calc(2, x, 200))

print("---------------------")
print((2**-1 + 2**-2 + 2**-3 + 2**-5 + 2**-6) * 4)