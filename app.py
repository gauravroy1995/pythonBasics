import random


# class Dice:
#
#     pi = 3
#
#     def __init__(self,numbers):
#         self.numbers = numbers
#
#     # def roll(self):
#     #      print(f"({random.choice(self.numbers)},{random.choice(self.numbers)})")
#     def area(self):
#         return self.numbers


class Dog():

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


class Cat(Dog):
    def __init__(self):
        Dog.__init__(self, 'aditi')


cat = Cat()
print(cat.print_name())