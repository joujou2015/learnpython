# def fib(n):
    # a, b = 0, 1
    # for _ in range(n):
        # a, b = b, a + b
        # yield a


# def main():
    # for val in fib(20):
        # print(val)


# if __name__ == '__main__':
    # main()
    
# def main():
    # str1 = 'hello, world!'
    # print(len(str1))
    # print(str1.capitalize())
    # print(str1.upper())
    # print(str1.find('or'))
    # print(str1.find('shit'))
    # print(str1.startswith('He'))
    # print(str1.startswith('hel'))
    # print(str1.endswith('!'))
    # print(str1.center(50, '*'))
    # print(str1.rjust(50,' '))
    # str2 = 'abc123456'
    # print(str2[2])
    # print(str2[2:5])
    # print(str2[2::])
    # print(str2[::2])
    # print(str2[::-1])
    # print(str2[-3:-1])
    # print(str2.isdigit())
    # print(str2.isalpha())
    # print(str2.isalnum())
    # str3 = '   jackfrued@126.com '
    # print(str3)
    # print(str3.strip())
    
# if __name__ == '__main__':
    # main()
    
    
# def main():
    # list1 = [1, 3, 5, 7, 100]
    # print(list1)
    # list2 = ['hello'] * 5
    # print(list2)
    # print(len(list1))
    # print(list1[0])
    # print(list1[4])
    # print(list1[-1])
    # print(list1[-3])
    # list1[2] = 300
    # print(list1)
    # list1.append(200)
    # list1.insert(1, 400)
    # list1 += [1000, 2000]
    # print(list1)
    # print(len(list1))
    # list1.remove(3)
    # if 1234 in list1:
        # list1.remove(1234)
    # del list1[0]
    # print(list1)
    # list1.clear()
    # print(list1)
    
    
# if __name__ == '__main__':
    # main()
    

# def main():
        # fruits = ['grape', 'apple', 'strawberry', 'waxberry']
        # fruits += ['pitaya','pear','mango']
        # for fruit in fruits:
            # print(fruit.title(), end=' ')
        # print()
        
        # fruits2 = fruits[1:4]
        # print(fruits2)
        # fruits3 = fruits[:]
        # print(fruits3)
        # fruits4 = fruits[-3:-1]
        # print(fruits4)
        # fruits5 = fruits[::-1]
        # print(fruits5)
        
        
# if __name__ == '__main__':
    # main()
    
    
    
# def main():
    # list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    # list2 = sorted(list1)
    # list3 = sorted(list1, reverse=True)
    # list4 = sorted(list1, key=len)
    # print(list1)
    # print(list2)
    # print(list3)
    # print(list4)
    # list1.sort(reverse = True)
    # print(list1)
    
    
# if __name__ == '__main__':
    # main()
    
    
# import sys

# def main():
    # f = [x for x in range(1,10)]
    # print(f)
    # f = [x + y for x in 'ABCDE' for y in '1234567']
    # print(f)
    # f = [x ** 2 for x in range(1,1000)]
    # print(sys.getsizeof(f))
    # print(f)
    # f = (x **2 for x in range(1,1000))
    # print(sys.getsizeof(f))
    # print(f)
    # for val in f:
        # print(val)
        

# if __name__=='__main__':
    # main()
    
    
    
# def main():
    # t = ('dong', 29, True, 'Nanjing')
    # print(t)
    # print(t[0])
    # print(t[3])
    # for member in t:
        # print(member)
    # t = ('wangdachui',20,True,'Kunming')
    # print(t)
    # person = list(t)
    # print(person)
    # person[0] = 'Bruce Lee'
    # person[1] = 25
    # print(person)
    # fruits_list = ['apple', 'banana', 'orange']
    # fruits_tuple = tuple(fruits_list)
    # print(fruits_tuple)
    
    
# if __name__=='__main__':
    # main()
    
    
    
# def main():
    # set1 = {1,2,3,3,3,2}
    # print(set1)
    # print('Length =', len(set1))
    # set2 = set(range(1,10))
    # print(set2)
    # set1.add(4)
    # set1.add(5)
    # set2.update([11,12])
    # print(set1)
    # print(set2)
    # set2.discard(5)
    # if 4 in set2:
        # set2.remove(4)
    # print(set2)
    
    # for elem in set2:
        # print(elem ** 2,end=' ')
    # print()
    # set3 = set((1,2,3,3,2,1))
    # print(set3.pop())
    # print(set3)
    # print(set1 & set2)
    # print(set1 | set2)
    # print(set1 - set2)
    # print(set1 ^ set2)
    # print(set2 <= set1)
    # print(set3 <= set1)
    # print(set1 >= set2)
    # print(set1 >= set3)
    
    
# if __name__ == '__main__':
    # main()
    

# def main():
        # scores = {'Dong': 95, 'Baiyuanfang': 78,'direnjie': 82}
        # print(scores['Dong'])
        # print(scores['direnjie'])
        # for elem in scores:
            # print('%s\t---->\t%d' %(elem, scores[elem]))
        # scores['Baiyuanfang'] = 65
        # scores['zhugewanglang'] = 71
        # scores.update(lengmian=67,fangqihe=85)
        # print(scores)
        # if 'wuzetian' in scores:
            # print(scores['wuzetian'])
        # print(scores.get('wuzetian'))
        # print(scores.get('wuzetian',60))
        # print(scores.popitem())
        # print(scores.popitem())
        # print(scores.pop('Dong', 100))
        # scores.clear()
        # print(scores)
            

# if __name__ == '__main__':
     # main()
            
            
            
# import  os
# import  time


# def main():
    # content = 'Welcome to Beijing......'
    # while True:
        # os.system('cls')
        # print(content)
        # time.sleep(0.2)
        # content = content[1:] + content[0]
    
    
# if __name__ == '__main__':
    # main()
    
    
    
# import random


# def generate_code(code_len=4):
    # """
    # Generate certain length verification code
    # :param code_len: length of the code(default length equal 4)
    # :return: the code contains random Capital and small letters
    # """
    # all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # last_pos = len(all_chars) -1
    # code = ''
    # for _ in range(code_len):
        # index = random.randint(0, last_pos)
        # code += all_chars[index]
    # return code
    
# print(generate_code())


# def max2(x):
    # m1,m2 = (x[0],x[1]) if x[0] > x[1] else (x[1],x[0])
    # for index in range(2,len(x)):
        # if x[index] > m1:
            # m2 = m1
            # m1 = x[index]
        # elif x[index] > m2:
            # m2 = x[index]
    # return m1, m2
    
# print(max2([1,2,6,12,17]))



# def is_leap_year(year):

    # return year % 4==0 and year % 100 != 0 or year % 400 == 0
    
# def which_day(year,month,date):
    # days_of_month = [
        # [31,28,31,30,31,30,31,31,30,31,30,31],
        # [31,29,31,30,31,30,31,31,30,31,30,31]
    # ][is_leap_year(year)]
    # total = 0
    # for index in range(month-1):
        # total += days_of_month[index]
    # return total + date
    
# def main():
    # print(which_day(1980,11,28))
    # print(which_day(1981,12,31))
    # print(which_day(2018,1,1))
    # print(which_day(2016,3,1))
    # print(which_day(2019,8,27))
    
# if __name__=='__main__':
    # main()
    
    
    
    
# def main():
    # num = int(input('Number of rowa: '))
    # yh = [[]] * num
    # for row in range(len(yh)):
        # yh[row] = [None] * (row + 1)
        # for col in range(len(yh[row])):
            # if col == 0 or col == row:
                # yh[row][col] = 1
            # else:
                # yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            # print(yh[row][col], end='\t')
        # print()
        
        
# if __name__ == '__main__':
        # main()




# from random import randrange, randint, sample


# def display(balls):
    # for index, ball in enumerate(balls):
        # if index == len(balls) -1:
            # print('|', end=' ')
        # print('%02d' % ball, end=' ')
    # print()
    
    
    
# def random_select():
    # red_balls = [x for x in range(1, 34)]
    # selected_balls =[]
    # selected_balls = sample(red_balls, 6)
    # selected_balls.sort()
    # selected_balls.append(randint(1,16))
    # return selected_balls
    
    
# def main():
    # n = int(input(' Machine selected: '))
    # for _ in range(n):
        # display(random_select())
        
        
# if __name__ == '__main__':
    # main()



# def main():
    # persons = [True] * 30
    # counter, index, number = 0,0,0
    # while counter < 15:
        # if persons[index]:
            # number += 1
            # if number == 9:
                # persons[index] = False
                # counter += 1
                # number = 0
        # index += 1
        # index %= 30 
    # for person in persons:
        # print('christ' if person else 'no-christ', end=' ')
        

# if __name__ == '__main__':
     # main()




import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])
    
    
# def main():
    # init_board = {
        # 'TL': ' ', 'TM': ' ', 'TR': ' ',
        # 'ML': ' ', 'MM': ' ', 'MR': ' ',
        # 'BL': ' ', 'BM': ' ', 'BR': ' '
    # }
    # begin = True
    # while begin:
        # curr_board = init_board.copy()
        # begin = False
        # turn = 'x'
        # counter = 0
        # os.system('clear')
        # print_board(curr_board)
        # while counter < 9:
            # move = input('It turns %s to move, please insert the position: ' % turn)
            # if curr_board[move] == ' ':
                # counter += 1
                # curr_board[move] = turn
                # if turn == 'x':
                    # turn = 'o'
                # else:
                    # turn = 'x'
            # os.system('clear')
            # print_board(curr_board)
        # choice = input('One more ?(yes|no)')
        # begin = choice == 'yes'
        
# if __name__ == '__main__':
    # main()






















        
    

    
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    