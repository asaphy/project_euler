def one():
	total = sum([x for x in range(0,1000) if x%5==0 or x%3==0])
	print(total)
one()