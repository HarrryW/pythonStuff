
def is_prime(candidate):
    for n in range(2, candidate):
        if candidate % n == 0:
            return False
    return True

#print(str(is_prime(23)))
#Prime Finder
divisor = 0
secDiv = 0
def primeFinder(x):
    for divisor in range (1,x+1):
        if(x%divisor==0 and divisor!=1):
            if not is_prime(divisor):
                break
            elif is_prime(divisor):
                print divisor
        else:
            continue
f = primeFinder(13195)
print(f)

#Learned a lot
