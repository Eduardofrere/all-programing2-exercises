""" Checks if a given number is a prime number 

args:
    strings of integers
    actual integers

return:
    either is prime or is not prime

Example:
    is_prime(7)
7 is prime
"""


def is_prime(n):
    divisors=[]
    if isinstance(n,(int,str)):
        try:
            n= int(n)
        except ValueError as e:
            raise ValueError("not a number")
    elif type(n) is float:
        raise ValueError("must be an integer")
    if n<= 1 :
        return n,"is not prime"
    for i in range(1,n+1):
        if n % i == 0:
            divisors.append(i)
    if divisors== [1,n]:
        return n, "is prime"
    else:
        return n, "is not prime"
print(is_prime(1)) 