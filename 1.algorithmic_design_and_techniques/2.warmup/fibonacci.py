# Uses python3
def calc_fib_r(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_lin(n):
	if (n <= 1):
		return n

	n_2 = 0
	n_1 = 1

	fib = 0

	for i in range(2,n + 1):
		fib = n_2 + n_1
		#print('{0} and {1}'.format(i, fib))
		n_2 = n_1
		n_1 = fib


	return fib

n = int(input())

#print(calc_fib_r(n))
print(calc_fib_lin(n))