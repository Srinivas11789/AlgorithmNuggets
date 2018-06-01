# Fibonacci

"""
n = 10

series = [0,1]

first = series[0]
second = series[1]

for i in range(n):
	next = first + second
	series.append(next)
	first = second
	second = next

print series
"""


def recur1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        value = recur1(n-1) + recur1(n-2)
        return value

memo = [0,1]
def recur(n):
    if n == 0:
	return 0
    elif n == 1:
	return 1
    elif n < len(memo):
        return memo[n]
    else:
        value = recur(n-1) + recur(n-2)
        memo.append(value)
        return value

import datetime
print datetime.datetime.now()
print recur1(40)
print datetime.datetime.now()
print recur(40)
print datetime.datetime.now()



