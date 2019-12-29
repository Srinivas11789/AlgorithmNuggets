# Logic 1: [String way] Convert to string and eval/math - 97% faster
# Initial type conversions
num = str(N)
n = len(num)
result = 0

# Armstrong calculation
for i in num:
	result += int(i)**n

# Decide result
if result == N:
	return True
else:
	return False
# Logic 2: [Only Int way] Find the size of the number or num of digit and perform calc - 88% faster
# * use modulo or div 

# Find the size of the number

n = 0
num = N
while num:
	n += 1
	num = num//10

# Armstrong calc - remove last digit and reduce number to the one without the last digit
armstrong = 0
num = N
while num:
	next_digit = num%10
	armstrong += next_digit**n
	num = num//10
	print(next_digit, armstrong, num, n)

if armstrong == N:
	return True
else:
	return False
