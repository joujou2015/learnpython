"""
输入M和N计算C(M,N)
"""

# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
    # fm *= num
# fn = 1
# for num in range(1, n + 1):
    # fn *= num
# fmn = 1
# for num in range(1, m - n + 1):
    # fmn *= num
# print(fm // fn // fmn)


"""
gcd lcm

Version 0.1
Autor: Dong
Date: 24/08/2019
"""


def gcd(x,y):
    (x,y) = (y,x) if x > y else (x,y)
    for factor in range (x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x,y)
    return x*y // gcd(x,y)


def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp %10
        temp //= 10
    return total == num

def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False
    

if __name__ == '__main__':
    num = int(input('Please insert a positive integrale: '))
    if is_palindrome(num) and is_prime(num)
        print('%d is prime paradromes' %num)
        
        
