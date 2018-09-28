a,b=1,1
sumEven = 0
while(a<100 and b < 100):
  a,b=b,a+b
  print a
  if(a%2==0):
    sumEven = sumEven + a
    print a
  else:
    continue
print("This one -> " + str(sumEven))

#Leanred that if you want to adjust two variables that are interdepented
#you must use a,b = b, a+b
