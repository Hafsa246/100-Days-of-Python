def prime_checker(n):
    is_prime = True
    for i in range(2,n-1):
        if(n%i == 0):
            is_prime = False

    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

n = int(input("Enter a number: "))
prime_checker(n)