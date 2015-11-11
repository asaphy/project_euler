def two(x,y,sum):
	z = x+y
	if z % 2 == 0:
		sum += z
	if z < 4000000:
		two(y,z,sum)
	else:
		print(sum)
two(1,2,2)