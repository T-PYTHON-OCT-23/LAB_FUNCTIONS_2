
def prime_num(val1:int,val2:int):
                for m in range(val1,val2 + 1):
                    if m > 1:
                        for i in range(2,m):
                             if (m % i)==0:
                              break
                        else:
                            print(m, end=" ")
        
num1 = int(input("Enter the first value :"))
num2 = int(input("Enter the second value: "))
prime_num(num1,num2)


