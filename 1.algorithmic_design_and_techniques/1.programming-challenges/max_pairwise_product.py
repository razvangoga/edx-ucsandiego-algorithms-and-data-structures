# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

maxmax = a[0]
lastmax = 0

for i in range(1, n):
	if a[i] > maxmax:
		lastmax = maxmax
		maxmax = a[i]
	elif a[i] > lastmax:
		lastmax = a[i]

print(maxmax * lastmax)