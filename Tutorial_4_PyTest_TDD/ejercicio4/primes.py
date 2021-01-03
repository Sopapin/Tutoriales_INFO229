
def is_prime(num):
	if num < 2:
		return False
	for n in range(2,math.floor(math.sqrt(n))):
		if num % n == 0:
			return False
	return True