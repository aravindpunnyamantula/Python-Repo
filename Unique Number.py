def Isunique(n):
    digits=set()
    while n:
        digit=n%10
        if digit in digits:
            return False
        digits.add(digit)
        n//=10
    return True

n=int(input())
if Isunique(n):
    print("Unique Number")
else:
    print("Not Unique Number")