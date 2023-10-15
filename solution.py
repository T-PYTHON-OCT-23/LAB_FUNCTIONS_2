def prime_number(num1:int,num2:int) -> print:
    
    for i in range(num1, num2):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)



prime_number(25,50)