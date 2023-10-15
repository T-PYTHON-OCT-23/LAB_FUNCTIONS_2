def find_primes (num1:int , num2:int) ->int:
     
      for i in range (num1 , num2):
         if i >1:
             for j in range(2,i):
                if (j % i) == 0:
                    break 
             else:
                res= f"{i} "
      return res    

num1 = 25
num2 = 50

result:int= find_primes(num1 , num2)
print= (f"The primes are: {result}")


