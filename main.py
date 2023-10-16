def find_primes( number1:int , number2:int):
    for i in range(number1, number2+1):  # two loops bc we have 2 numbers

        #to check if it's a prime or not
        for j in range (2, i):
            if i%j ==0:
                break
        else: 
            print(f"{i} is prime number.")

find_primes(25,50)