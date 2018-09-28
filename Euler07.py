"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""


def is_prime(candidate):
    for n in range(2, candidate):
        if candidate % n == 0:
            return False
    return True
def primeFinder():
    primeList = []
    i=0
    for y in range(2,1000000):
        if is_prime(y):
            i += 1
            if i == 10001:
                print y
                break
            else:
                continue
        else:
            continue

primeFinder()
