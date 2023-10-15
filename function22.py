def prime(num: int):
    if num <= 2:
        return True
    if num <= 1:
        return False
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(start, end):
    if start <= 1:
        start = 2

    for num in range(start, end + 1):
        if prime(num):
            print(num)


start_number = int(input("start number is: "))
end_number = int(input(" end number is: "))
print("Prime numbers between", start_number, "and", end_number, "are:")
find_primes(start_number, end_number)
