def is_prime(n):
  """Returns True if n is a prime number, fulse if is not."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def find_primes(num1 : int,num2 : int) -> int:

    output=""

    for n in range(num1,num2):
        #useing function is_prime() to check the number is prime or not
        
        if is_prime(n) == True:
             output +=f"{str(n)}\n"
                       
    return output
             


result=find_primes(29,50)
print(result)