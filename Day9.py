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

































































   