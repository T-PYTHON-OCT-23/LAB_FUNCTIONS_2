def find_primes(par1:int ,par2:int)->str:
    output=f"These are the prime numbers between {par1} and {par2}: "
    for i in range(par1,par2+1):
        count=0
        for j in range(1,i):
            if i%j==0:
                count+=1
        if count==1:
            output+= str(i)+","
    return output   
print(find_primes(0,100))

