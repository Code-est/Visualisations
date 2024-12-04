from random import randint


class Die():
#""" ласс, представл€ющий один кубик."""  

    def __init__(self, num_sides=6):
        #"""ѕо умолчанию используетс€ шестигранный кубик."""
        self.num_sides = num_sides

    def roll(self):
        #""""¬озвращает случайное число от 1 до числа граней."""
        return randint(1, self.num_sides)
    

