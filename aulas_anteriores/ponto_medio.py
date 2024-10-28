def f(x):
	return pow(x, 2) - 5




i = 0
imax = 100
left = 2
right = 3
mid = (left+right)/2
tolerancia = 1e-6

while (abs((f(right)-f(left))/2) > tolerancia and i < imax):
	if (f(left)*f(mid) > 0):
		left = mid
	else:
		right = mid
	mid = (left+right)/2
	i += 1

print("{:d}, {:.6f}, {:.6f} ".format(i, mid, f(mid)))