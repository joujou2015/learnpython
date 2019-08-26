"""
Narcissistic number

Version:0.1
Autor:Dong
Date:2019/08/23
"""

# def Narcissistic(num):
    # s = str(num)
    # length = len(s)
    # count = length
    # sum_num = 0
    # while count:
        # sum_num += int(s[count-1])**length
        # count -= 1
    # else:
        # if sum_num == num:
            # print('%d is a %d bit narcissistic number ' % (num, length))
        # else:
            # print('%d is not a narcissistic number' % num)
            

# max_num = int(input('Please insert the max numner: '))
# for num in range(0,max_num):
    # Narcissistic(num)
    
    
    


"""
Find the perfect number in range 1-9999

Version 0.1
Autor: Dong
Date:2019-08-24
"""

# import math

# for num in range(1,10000):
    # result = 0
    # for factor in range(1,int(math.sqrt(num)+1)):
        # if num % factor == 0:
            # result += factor
            # if factor > 1 and num // factor != factor:
                # result += num // factor
    # if result == num:
        # print(num)
        
        
        
"""
Hundred coins to buy one hundred chicken

Version 0.1
Autor: Dong
Date:24/08/2019
"""

# for x in range(0,20):
    # for y in range(0,33):
        # z = 100-x-y
        # if 5*x + 3*y + z/3 == 100:
            # print('cock: %d, hen: %d, baby chicken: %d ' % (x,y,z))
            
            
"""
Filbonacci sequence

Version 0.1
Autor: Dong
Date:24/08/2019
"""

a = 0
b = 1
for _ in range(20):
    a, b = b, a+b
    print(a, end=' ')
    
    
"""
Craps diceing game

Version 0.1
Autor: Dong
Date:24/08/2019
"""

# from random import randint
# money = 1000
# while money > 0:
    # print('Your total asset: ', money)
    # needs_go_on = False
    # while True:
        # debt = int(input('Please debt: '))
        # if 0 < debt <= money:
            # break
    # first = randint(1,6) + randint(1,6)
    # print('player has %d point' % first)
    # if first == 7 or first == 11:
        # print ('Player wins!!')
        # money += debt
    # elif first == 2 or first == 12:
        # print('The host win!')
        # money -= debt
    # else:
        # needs_go_on = True
    
    # while needs_go_on:
        # current = randint(1,6) + randint(1,6)
        # print('player has %d point' % current)
        # if current == 7:
            # print('The host win!')
            # money -= debt
            # needs_go_on = False
        # elif current == first:
            # print('The player wins!!!')
            # money += debt
            # needs_go_on = False

# print('Your are broken, game over!!')
            