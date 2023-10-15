def find_primes(num1:int ,num2:int) -> int:

    for n in range(num1,num2+1):
        for n2 in range(2,n):
            if n%n2==0:
                break
        else:
            print(n)
number1=int(input("please enter the first number: "))
number2=int(input("please enter the second number: "))             
find_primes(number1,number2)    

