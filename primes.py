
def primes():
    M =[]
    for i in range(25,50):
        for j in range(2,i):
         if i%j==0:
            break
        else :
         M.append(i)
    print(M)

primes()


