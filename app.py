import random


class Dice:

    def __init__(self,numbers):
        self.numbers = numbers

    def roll(self):
         print(f"({random.choice(self.numbers)},{random.choice(self.numbers)})")

