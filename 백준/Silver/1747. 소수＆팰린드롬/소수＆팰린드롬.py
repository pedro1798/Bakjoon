from sys import stdin
import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False # 소수가 아님
    return True

a = int(stdin.readline())

tf = True
while tf:
    if isPrime(a):
        if len(str(a)) > 1:
            rev = str(a)[::-1]
            if str(a)[0: len(str(a)) // 2] == rev[0: len(str(a)) // 2]:
                print(a, end = " ")
                tf = False
            else:
                a += 1
                pass
        elif len(str(a)) == 1 and a != 1 and a != 0:
            print(a, end = " ")
            tf = False
        elif a == 1 or a == 0:
            a += 1
            pass
    else:
        a += 1
