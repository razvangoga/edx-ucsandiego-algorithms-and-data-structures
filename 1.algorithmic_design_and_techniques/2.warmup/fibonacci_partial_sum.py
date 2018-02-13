# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fibonacci_partial_sum(from_, to):
    last_digit_from = get_fibonacci_huge_with_pisano_sequence(from_ + 1, 10)

    if last_digit_from == 0:
        last_digit_from = 10

    last_digit_from -= 1

    last_digit_to = get_fibonacci_huge_with_pisano_sequence(to + 2, 10)

    if last_digit_to == 0:
        last_digit_to = 10

    last_digit_to -= 1

    if last_digit_to < last_digit_from:
        last_digit_to += 10

    return last_digit_to - last_digit_from

def calc_fib_lin(n):
    if (n <= 1):
        return n

    n_2 = 0
    n_1 = 1

    fib = 0

    for i in range(2,n + 1):
        fib = n_2 + n_1
        n_2 = n_1
        n_1 = fib

    return fib

def get_fibonacci_huge_with_pisano_sequence(n, m):
    if (n <= 1):
        return n

    n_2 = 0
    n_1 = 1

    fib = 0

    sequence_length = 2

    while 1 == 1:
        fib = n_2 + n_1
        n_2 = n_1
        n_1 = fib

        if n_2 % m == 0 and n_1 % m == 1:
            sequence_length -= 1
            break
        else:
            sequence_length += 1

    small_fib = n % sequence_length

    return calc_fib_lin(small_fib) % m

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))