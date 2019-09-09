# class Person(object):
    # def __init__(self, name, age):
        # self._name = name
        # self._age = age
        
    # @property
    # def name(self):
            # return self._name
            
    # @property
    # def age(self):
        # return self._age
            
    # @age.setter
    # def age(self, age):
        # self._age = age
            
    # def play(self):
        # if self._age <= 16:
            # print('%s is playing flying chess.' % self._name)
        # else:
            # print('%s is playing cards.' % self._name)


# def main():
    # person = Person('Wangdachui', 12)
    # person.play()
    # person.age = 22
    # person.play()
    # #person.name = 'Baiyuanfang'


# if __name__ == '__main__':
    # main()
   
# from math import sqrt

# class Triangle(object):
    # def __init__(self, a, b, c):
        # self._a = a
        # self._b = b
        # self._c = c
        
    # @staticmethod
    # def is_valid(a, b, c):
        # return a + b > c and b + c > a and a + c > b
        
    # def perimeter(self):
        # return self._a + self._b + self._c
        
    # def area(self):
        # half = self.perimeter()/2
        # return sqrt(half * (half - self._a)) * (half - self._b)* (half -self._c)
        
        
# def main():
    # a, b, c = 3, 4, 5
    # if Triangle.is_valid(a,b,c):
        # t = Triangle(a,b,c)
        # print(t.perimeter())
        # print(t.area())
    # else:
        # print('can not create to be a triangle.')
        
# if __name__ == '__main__':
    # main()


# from time import time, localtime, sleep


# class Clock(object):
    # """Numerical clock
    # """
    
    # def __init__(self, hour=0, minute=0, second=0):
        # self._hour = hour
        # self._minute = minute
        # self._second = second
        
    # @classmethod
    # def now(cls):
        # ctime = localtime(time())
        # return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
        
    # def run(self):
        # self._second += 1
        # if self._second == 60:
            # self._second = 0
            # self._minute += 1
            # if self._minute == 60:
                # self._minute = 0
                # self._hour += 1
                # if self._hour == 24:
                    # self._hour = 0
                    
    # def show(self):
        # """ show the time"""
        # return '%02d:%02d:%02d' % \
            # (self._hour, self._minute, self._second)
            

# def main():
    # clock = Clock.now()
    # while True:
        # print(clock.show())
        # sleep(1)
        # clock.run()
        
        
# if __name__ == '__main__':
    # main()
    

# class Person(object):
    # """person"""
    
    # def __init__(self, name, age):
        # self._name = name
        # self._age = age
        
    # @property
    # def name(self):
        # return self._name
        
    # @property
    # def age(self):
        # return self._name
        
    # @age.setter
    # def age(self, age):
        # self._age = age
        
    # def play(self):
        # print('%s is happily playing.' % self._name)
        
    # def watch_av(self):
        # if self._age >=18:
            # print('%s is watching av.' %self._name)
        # else:
            # print('%s can only watch <<lovely bear>>.' % self._name)
            
# class Student(Person):
    # """student"""
    
    # def __init__(self, name, age, grade):
        # super().__init__(name, age)
        # self._grade = grade
        
    # @property
    # def grade(self):
        # return self._grade
        
    # @grade.setter
    # def grade(self, grade):
        # self._grade = grade
        
    # def study(self, course):
        # print('%s of %s is studying %s. ' % (self._grade, self._name, course))
        

# class Teacher(Person):
    # """Teacher"""
    
    # def __init__(self, name, age, title):
        # super().__init__(name, age)
        # self._title = title
        
    # @property
    # def title(self):
        # return self._title
        
    # @title.setter
    # def title(self, title):
        # self._title = title
        
    # def teach(self, course):
        # print('%s%s is teaching %s. ' % (self._title, self._name, course))
        
        
# def main():
    # stu = Student('Wangdachui', 15, 'Ninth grade')
    # stu.study('Math')
    # stu.watch_av()
    # t = Teacher('Dong', 29, 'Prof.')
    # t.teach('Python programming')
    # t.watch_av()
    
    
# if __name__ == '__main__':
    # main()
    
   
      
   
# from abc import ABCMeta, abstractmethod


# class Pet(object, metaclass=ABCMeta):

    # def __init__(self, nickname):
        # self._nickname = nickname
            
    # @abstractmethod
    # def make_voice(self):
        # """make sound"""
        # pass
            
# class Dog(Pet):
    # """Dog"""
    
    # def make_voice(self):
        # print('%s: Wa,wa,wa... ' % self._nickname)
        
# class Cat(Pet):
    # """cat"""
    
    # def make_voice(self):
        # print('%s: miao...miao...' % self._nickname)
        
# def main():
    # pets = [Dog('Wangcai'), Cat('Ketty', Dog('Dashang')]
    # for pet in pets:
        # pet.make_voice()
        
        
# if __name__ == '__main__':
    # main()
    
    
    
from abc import ABCMeta, abstractmethod
from random import randint,randrange

class Fighter(object, metaclass=ABCMeta):
    __slot__ = ('_name', '_hp')
    
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp
        
    @property
    def name(self):
        return self._name
        
    @property
    def hp(self):
        return self._hp
        
    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0
        
    @property
    def alive(self):
        return self._hp > 0
        
    @abstractmethod
    def attack(self, other):
        pass
        
class Ultraman(Fighter):
    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp
        
    def attack(self, other):
        other.hp -= randint(15, 25)
        
    def huge_attack(self, other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False
            
    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -=20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False
            
    def resume(self):
        incr_point = randint(1,10)
        self._mp += incr_point
        return incr_point
        
    def __str__(self):
        return '---%s ultraman ---\n'% self._name + \
        'hp: %d\n' % self._hp + \
        'mp: %d\n' % self._mp 
        
# class Monster(Fighter):
    # __slot__ = ('_name', '_hp')
    
    # def attack(self, other):
        # other.hp -= randint(10, 20)
        
    # def __str__(self):
        # return '---%s monster---\n' % self._name +\
            # 'hp: %d\n' % self._hp
            
# def is_any_alive(monsters):
    # for monster in monsters:
        # if monster.alive > 0:
            # return True
    # return False
        
# def select_alive_one(monsters):
    # monsters_len = len(monsters)
    # while True:
        # index = randrange(monsters_len)
        # monster = monsters[index]
        # if monster.alive > 0:
            # return monster
                
# def display_info(ultraman, monsters):
    # print(ultraman)
    # for monster in monsters:
        # print(monster, end='')
            
# def main():
    # u = Ultraman('Dong', 1000, 120)
    # m1 = Monster('Direnjie', 250)
    # m2 = Monster('Baiyuanfang', 500)
    # m3 = Monster('Wangdachui', 700)
    # ms = [m1, m2, m3]
    # fight_round = 1
    # while u.alive and is_any_alive(ms):
        # print('========il %02d turn=====' % fight_round)
        # m = select_alive_one(ms)
        # skill =  randint(1, 10)
        # if skill <= 6:
            # print('%s is using normal attack to %s.' % (u.name, m.name))
            # u.attack(m)
            # print('%s resume %d mp' %(u.name, u.resume()))
        # elif skill <=9:
            # if u.magic_attack(ms):
                # print('%s is using magic attack.' % u.name)
            # else:
                 # print('%s is failed to use magic attack.' % u.name)
        # else:
            # if u.huge_attack(m):
                # print('%s is using huge attack to %s.' % (u.name, m.name))
            # else:
                # print('%s is using normal attack to %s.' % (u.name, m.name))
                # print('%s magic resume %d points.' % (u.name, u.resume()))
        # if m.alive > 0:
            # print('%s fight back to %s.' %(m.name, u.name))
            # m.attack(u)
        # display_info(u, ms)
        # fight_round +=1
    # print('\n========flight is over======')
    # if u.alive > 0:
        # print('%s ultraman wins!' % u.name)
    # else:
        # print('monster wins!')
 

# if  __name__ == '__main__':
    # main()
    
    
# import random

# class Card(object):
    # def __init__(self, suite, face):
        # self._suite = suite
        # self._face = face
        
    # @property
    # def face(self):
        # return self._face
        
    # @property
    # def suite(self):
        # return self._suite
    
    # def __str__ (self):
        # if self._face == 1:
            # face_str = 'A'
        # elif self._face == 11:
            # face_str = 'J'
        # elif self._face == 12:
            # face_str = 'Q'
        # elif self._face == 13:
            # face_str = 'K'
        # else:
            # face_str = str(self._face)
        # return '%s%s' % (self._suite, face_str)
        
    # def __repr__(self):
        # return self.__str__()
        
# class Poker(object):
    # def __init__(self):
        # self._cards = [Card(suite, face)
                        # for suite in '♠♥♣♦'
                        # for face in range(1,14)]
        # self._current = 0
        
    # @property
    # def cards(self):
        # return self._cards
        
    # def shuffle(self):
        # self._current = 0
        # self._current < len(self._cards)
        
    # @property
    # def next(self):
        # card = self._cards[self._current]
        # self._current += 1
        # return card
        
    # @property
    # def has_next(self):
        # return self._current < len(self._cards)
        
# class Player(object):
    # def __init__(self, name):
        # self._name = name
        # self._cards_on_hand = []
        
    # @property
    # def name(self):
        # return self._name
        
    # @property
    # def cards_on_hand(self):
        # return self._cards_on_hand
    
    # def get(self, card):
        # self._cards_on_hand.append(card)
       
    # def arrange(self, card_key):
        # self._cards_on_hand.sort(key = card_key)
        

# def get_key(card):
    # return(card.suite, card.face)
    
# def main():
    # p = Poker()
    # p.shuffle()
    # players = [Player('Dong'), Player('Xi'), Player('Nan'), Player('Bei')]
    # for _ in range(13):
        # for player in players:
            # player.get(p.next)
    # for player in players:
        # print(player.name + ':', end= ' ')
        # player.arrange(get_key)
        # print(player.cards_on_hand)
        
# if __name__ == '__main__':
    # main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    































































   