
def find_primes(num1:int,num2:int):
    for x in range(num1,num2+1):
        if (x>1):
             for y in range(2,x):
                 if x%y==0:
                     break
             else:
                print(x)
    
      
print(find_primes(25,50))