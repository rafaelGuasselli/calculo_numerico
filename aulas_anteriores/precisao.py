import numpy as np
p = 1
c = 1
while (True):
	p /= 2
	if (p+np.float32(1) > 1):
		c+=1
	else:
		break
print(f"p: ${p}, c: {c}")