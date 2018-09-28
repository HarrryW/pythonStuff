for x in range(100,1000):
    for n in range(100,1000):
        if int(str(x*n)[::-1])==x*n:
            print x*n
            break
        else:
            continue
#Learned to inverse a string with [::-1]