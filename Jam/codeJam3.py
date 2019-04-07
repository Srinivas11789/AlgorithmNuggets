def is_a_prime(number):
    #import math
    # Assume number is odd, Neglecting 1 and number itself
    # 2 is the only even prime
    if number%2 == 0:
        return False
    #for i in range(3, int(math.sqrt(number))+1, 2):
    for i in range(3, int(number**(1/2.0))+1, 2):
        if number%i == 0:
            return False
    return True

def prime_list_under(N):
    # Get All the Prime Numbers
    # Just get the first 2 primes to get this done... --> this would work when the plaintext is ABC in order?
    # Iterate only odd number --> potential prime candidates
    primes = []
    for i in range(3, N+1, 2):
        if is_a_prime(i):
            #if target//i in primes:
            #    return i, target//i
            #else:
            primes.append(i)
    return primes

def decrypt(N, ciphertext):
    # Get all the primes under N
    # get first 2 primes to calculate others? Wont work
    primes = prime_list_under(N)
    #print primes
    crypto_key = [] # Selected primes
    # Find the First prime that is divisible here
    target = int(ciphertext[0])
    #for prime in primes:
    #    if target%prime == 0:
    #        crypto_key.append(prime)
    #        crypto_key.append(target//prime)
    #        break
    k = 0
    while target%primes[k] != 0:
        k += 1
    crypto_key.append(primes[k])
    crypto_key.append(target//primes[k])
    if len(ciphertext) > 1 and int(ciphertext[1])%crypto_key[0] == 0:
        crypto_key = crypto_key[::-1]
    #print crypto_key    
    next = crypto_key[-1]
    count = 1
    while count < len(ciphertext):
        next = int(ciphertext[count])//next
        #print ciphertext[count], crypto_key[-1], next, crypto_key
        crypto_key.append(next)
        count += 1
    """
    stack = [crypto_key[-1], target//crypto_key[-1]]
    while stack:
        current = stack.pop(0)
        if current not in crypto_key:
            crypto_key.append(current)
        for cipher in ciphertext:
            if int(cipher)%current == 0 and (int(cipher)//current not in crypto_key):
                stack.append(int(cipher)//current)
    """
    alphabets = sorted(set(crypto_key))
    #print crypto_key, alphabets
    result = ""
    for c in crypto_key:
        result += chr(65+alphabets.index(c))
    return result


# Encryption Scheme
# * Given N and Length of the ciphertext
# * Ans:
# * Length og the plaintext is len(ciphertext)+1
# * Choose prime numbers (26) upto N and compute product of adjacent numbers

"""
# Input Format
2
103 31
217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053
10000 25
3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543
"""
tcs = raw_input()
for i in range(int(tcs)):
    N, L = raw_input().split(" ")
    ciphertext= raw_input().split(" ")
    print ciphertext, N, L
    if len(ciphertext) != int(L):
        print "Case #"+str(i+1)+": "+"Length Not Equal!"
    else:
        print "Case #"+str(i+1)+": "+decrypt(int(N), ciphertext)