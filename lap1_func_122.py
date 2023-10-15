def find_primes(start, end):
    for num in range(start, end + 1):
       for i in range (num , num+1 ):
        if num % 2!=0:
            print(num)


find_primes(25, 50)