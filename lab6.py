
def find_primes (first_parameter:int , second_parameter:int)->int :
    #prime_number = int(input("Enter Prime Number: "))
    number=[]
    for nummber1 in range(first_parameter,second_parameter):
       for number2 in range(2,nummber1):
          if nummber1 % number2 == 0 :
             break
          
       else:
          number.append(nummber1)
        
    return number
prime_number = find_primes(25,50)
print(prime_number)


        
       





'''
def find_primes (first_parameter:int , second_parameter:int)->int :
  number:int= first_parameter , second_parameter
  if number :
       for n in number :
        if n/n==1 and n/1==n:
            print(n , "is prime number")
            number.append(number)

  else:
        print("The number is not prime number. ")
    
        return number

#result = find_primes(first_parameter=25, second_parameter=50)
#print("result is: ", result)
print(find_primes(25,50))
'''