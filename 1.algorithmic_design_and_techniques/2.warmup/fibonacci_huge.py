# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

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
    n_2 = 0
    n_1 = 1

    fib = 0

    #sequence = [None] * m
    #sequence[0] = n_2 % m
    #sequence[1] = n_1 % m

    sequence_length = 2

    for i in range(2,n + 1):
        fib = n_2 + n_1
        n_2 = n_1
        n_1 = fib

        if n_2 % m == 0 and n_1 % m == 1:
            #sequence = sequence[:-1]
            #del sequence[i - 1]
            sequence_length -= 1
            break
        else:
            sequence_length += 1
            #sequence[i] = fib % m

    #sequence_length = len(sequence) - 1
    #print(sequence_length)
    small_fib = n % sequence_length
    #return sequence[small_fib]
    return calc_fib_lin(small_fib) % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    #print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_with_pisano_sequence(n,m))