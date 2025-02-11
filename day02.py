from operator import truediv

n = int(input("Input number : "))

is_prime = False

if n>=2:
    count = 0
    for i in range(2, n):
        if n % i == 0:
            # count = count + 1
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(f"{n} is prime numer")
else:
    print(f"{n} is NOT prime number")
9
