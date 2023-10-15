

def from_to (num1:int , num2:int) -> int :
    """All numbers except the initial numbers are printed"""
    my_range=range(num1,num2+1)
    rang = range(2 , num2+1)
    
    for n in my_range: 
        for n2 in rang: 
            if not n == n2:   
                result = n / n2
                cheek = str(result).split('.')
                if cheek[1] == '0' :
                    print(n)
                    break
        
        
   
from_to(25,50)

