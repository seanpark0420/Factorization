from datetime import datetime
import math
total = 0

def isPrime(a):
    global total
    w=0#약수의 개수
    for i in range(math.trunc(math.sqrt(a))):
        total+=1
        if a%(i+1)==0:
            w+=1
    return w==1
a=int(input("숫자입력"))
print(datetime.now())
p=[] # 소인수 값을 넣을 때
for i in range(a):
    k=0 #소수의 지수
    if isPrime(i+1) and i>0:
        x=i+1
        total += 1
        while a%x ==0:
            total+=1
            k+=1
            x *=(i+1)
        if k>0:
          p.append((i+1,k))
print(datetime.now(),p,total)