from cmath import sqrt

def sign(val):
	return val/abs(val)

def nextX(a, b, c, x):
	top = 2 * c	
	delta = b*b - 4*a*c
	return x - (top/(b + sign(b) * sqrt(delta)))

def f(x):
	return  x**4 - 3*(x**3) + x**2 + x + 1

def q(a,b):
	return (f(a)-f(b))/(a-b)


def run(x0, x1, x2):
	tolerancia = 1e-8
	imax = 100
	i = 0

	while abs(f(x0)) > tolerancia and i < imax:
		a = (q(x0, x2) - q(x1, x2))/(x0 - x1)
		b = (q(x0, x2) * (x2-x1) + q(x1, x2) * (x0-x2))/(x0 - x1)
		c = f(x2)

		nx2 = nextX(a, b, c, x2)
		x0, x1 = x1, x2
		x2 = nx2
		i+=1

	return x2

real1 = run(0.5, 1, 2)
print(real1.real)

real2 = run(1.5, 2, 2.5)
print(real2.real)

complexa = run(-0.5, 0, 0.5)
print(complexa)