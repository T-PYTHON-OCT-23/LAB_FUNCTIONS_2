def primeNumbers( n1:int , n2:int):
    for numbers in range(n1 , n2+1):
        for n in range(2, numbers):
           if numbers % n == 0:
                break
        else:
            print(numbers)
            
           
    

primeNumbers(25 , 50)


               

    