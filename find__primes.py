def find_primes(num1:int ,num2:int) -> int:

    for n in range(num1,num2+1):
        if n % 2 != 0 and n%3 != 0 and n%4 !=0 and n%5 != 0 and n%6 !=0 and n%7 !=0 and n%8 !=0 and n%9 !=0 :
          
            print (n) 
number1=int(input("please enter the first number: "))
number2=int(input("please enter the second number: "))             
find_primes(number1,number2)    

