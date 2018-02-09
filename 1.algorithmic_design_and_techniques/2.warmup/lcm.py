# Uses python3
import sys
import math

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

#faster
def lcm_by_factors(a,b):
	factors = {}

	factors_a = get_factors(a)
	factors_b = get_factors(b)

	for i, (k, v) in enumerate(factors_a.items()):
		if k in factors:
			if factors[k] < v:
				factors[k] = v
		else:
			factors[k] = v

	for i, (k, v) in enumerate(factors_b.items()):
		if k in factors:
			if factors[k] < v:
				factors[k] = v
		else:
			factors[k] = v

	lcm = 1
	for i, (k, v) in enumerate(factors.items()):
		lcm *= int(math.pow(k, v))

	#print(factors)

	return lcm

def get_factors(n):
	factors = {}

	while n > 1:
		
		x = False

		for i in range(2, n + 1):
			x = True
			if( n % i == 0):
				if i in factors:
					factors[i] += 1
				else:
					factors[i] = 1

				n = n // i
				break

		if not x:
			if n in factors:
				factors[n] += 1
			else:
				factors[n] = 1
			break

	return factors


#fastest
def lcm_euclid(a, b):
	return a * b // gcd_euclid(a, b)


def gcd_euclid(a,b):
	if b == 0:
		return a

	return gcd_euclid(b, a % b)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    #print(lcm_naive(a, b))
    #print(lcm_by_factors(a, b))
    print(lcm_euclid(a,b))