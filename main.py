import math
def isPrime(n):
    for i in range(2, int(math.isqrt(n)) + 1):
        q, r = divmod(n, i)
        if r == 0:
            return False  # Found a factor, not prime
    return True  # No factors found, prime


def findprime():
    findprimes = int(input("Enter the first number: "))
    find2primes = int(input("Enter the second number: "))
    list_=[]
    for i in range(findprimes, find2primes):
        if isPrime(i):
            list_.append(i)
    return list_            
        
def camlecase(sentence):
    if type(sentence) == str:
        for i in sentence:
            if i.isupper():
                sentence = sentence.replace(i, " " + i.lower())
        return sentence

print(findprime())
print(camlecase("helloWorldThere"))
    
