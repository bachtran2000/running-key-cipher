
from math import gcd

def isPrime(a):
    if a <= 1:
        return False
    else:
        for i in range(2,a//2):
            if a % i == 0:
                return False
        return True

def phi(n):
    if isPrime(n):
        print('Phi of',n, "is", n-1) 
    else:
        arr_re = []
        result = 1
        for i in range(2,n):
            if (gcd(i, n) == 1):
                result += 1
                arr_re.append(i)
        print('Phi of',n, "is", result)        


for i in range(1,101):
    phi(i)