def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
d1=int(input())
d2=int(input())
d3=d1+d2
i=d3+1
count=1
while True:
    if prime(i):
        break
    count+=1
    i+=1
print(count)
