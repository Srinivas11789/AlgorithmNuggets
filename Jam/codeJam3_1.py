def is_a_prime(number):
    if number%2 == 0:
        return False
    for i in range(3, int(number**(1/2.0))+1, 2):
        if number%i == 0:
            return False
    return True

def prime_list_under(N):
    primes = [2]
    for i in range(3, N+1, 2):
        if is_a_prime(i):
            primes.append(i)
    return primes

def decrypt(N, ciphertext):
    primes = prime_list_under(N)
    print primes
    crypto_key = []
    future = None
    while ciphertext:
        target = int(ciphertext.pop(0))
        if not crypto_key and not future:
            p = 0
            while p < len(primes) and future == None:
                if target%primes[p] == 0 and target//primes[p] in primes:
                    future = target//primes[p]
                p += 1
            crypto_key.append(primes[p-1])
            crypto_key.append(future)
            if len(ciphertext) > 1:
                if int(ciphertext[1])%crypto_key[0] == 0:
                    crypto_key = crypto_key[::-1]
            future = crypto_key[-1]
        else:
            if future and target//future in primes:
                crypto_key.append(target//future)
                future = crypto_key[-1]

    alphabets = sorted(set(crypto_key))
    result = ""
    for c in crypto_key:
        result += chr(65+alphabets.index(c))
    print crypto_key, alphabets
    return result

tcs = raw_input()
for i in range(int(tcs)):
    N, L = raw_input().split(" ")
    ciphertext= raw_input().split(" ")
    #print ciphertext, N, L
    if ciphertext == "":
        print "Case #"+str(i+1)+": "+""
    elif len(ciphertext) != int(L):
        print "Case #"+str(i+1)+": "+"Length Not Equal!"
    else:
        print "Case #"+str(i+1)+": "+decrypt(int(N), ciphertext)