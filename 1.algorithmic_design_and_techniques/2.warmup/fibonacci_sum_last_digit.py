# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

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

def get_fibonacci_huge_with_pisano_sequence(n, m):
    if (n <= 1):
        return n

    n_2 = 0
    n_1 = 1

    fib = 0

    n += 2

    sequence_length = 2

    for i in range(2,n + 1):
        fib = n_2 + n_1
        n_2 = n_1
        n_1 = fib

        if n_2 % m == 0 and n_1 % m == 1:
            sequence_length -= 1
            break
        else:
            sequence_length += 1

    small_fib = n % sequence_length

    last_digit = calc_fib_lin(small_fib) % m

    if last_digit == 0:
        return  9
    else:
        return last_digit - 1


def get_fibonacci_sum_list(n):
    if (n <= 1):
        return n

    n_2 = 0
    n_1 = 1

    print('{0:3d} | {1:25d} | {2} | {3:25d} | {4}'.format(n_2, n_2, n_2, n_2, n_2))
    print('{0:3d} | {1:25d} | {2} | {3:25d} | {4}'.format(n_1, n_1, n_1, n_1, n_1))

    fib = 0
    sum = 1
    for i in range(2,n + 3):
        fib = (n_2 + n_1)
        sum += fib
        print('{0:3d} | {1:25d} | {2} | {3:25d} | {4}'.format(i, fib, fib % 10, sum, sum % 10))
        n_2 = n_1
        n_1 = fib

    return fib

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    #print(get_fibonacci_sum_list(n))
    print(get_fibonacci_huge_with_pisano_sequence(n, 10))