from operator import truediv

n = int(input("Input number : "))

is_prime = False

if n>=2:
    #count = 0
    is_prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            # count = count + 1
            is_prime = False
            break
        #print(i, end=' ')
else:
    is_prime = False

if is_prime:
    print(f"{n} is prime numer")
else:
    print(f"{n} is NOT prime number")