def find_primes(num1:int,num2:int):
    for num in range(num1,num2+1):
       if is_prime(num):
           print(num)



def is_prime(num:int):
    if num<2:
        return False                 
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
          
find_primes(25,50)