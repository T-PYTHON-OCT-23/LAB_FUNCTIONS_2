## Create a function : find_primes that takes in 2 parameters of type int , and print the prime numbers between the first parameter and the second parameter . 

def find_primes(start: int, end: int):
    prime_list = []

    for num in range(start, end + 1):
        if num > 1:  # Prime numbers must be greater than 1
            for num2 in range(2, num):
                if num % num2 == 0:
                    break
           
            else:
                prime_list.append(num)

    return prime_list

num1 = int(input("Enter start number: "))
num2 = int(input("Enter end number: "))


prime_list = find_primes(num1, num2)
print(prime_list)
