

def isPrime(a,n):
   for i in range(a, n+1):
        z=0
        for j in range(2,i):
           if (i%j== 0):
               z=1
               break
        if z==0:
            print(i)
            
          
a = int(input("Enter first number: "))
n = int(input("Enter second number: "))
isPrime(a,n)

