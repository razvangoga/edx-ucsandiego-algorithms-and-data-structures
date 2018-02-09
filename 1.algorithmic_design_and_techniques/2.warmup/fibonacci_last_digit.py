# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit(n):
    if (n <= 1):
        return n

    n_2 = 0
    n_1 = 1

    fib = 0

    for i in range(2,n + 1):
        fib = (n_2 + n_1) % 10
        #print('{0} and {1}'.format(i, fib))
        n_2 = n_1
        n_1 = fib


    return fib

#if __name__ == '__main__':
#    input = sys.stdin.read()
n = int(input())
#print(get_fibonacci_last_digit_naive(n))
print(get_fibonacci_last_digit(n))