import random


class AMRAPWOD:
    def __init__(self, first_exercise, second_exercise, third_exercise):
        self.first_exercise = first_exercise
        self.second_exercise = second_exercise
        self.third_exercise = third_exercise

    def print(self):
        print('1. {}\n2. {}\n3. {}'.format(self.first_exercise.print(), self.second_exercise.print(), self.third_exercise.print()))


class Exercise:
    def __init__(self, desc, type, units, amount, logger):
        self.description = desc
        self.type = type
        self.units = units
        self.logger = logger
        self.amount = amount

    def print(self):
        return '{}: {} {}'.format(self.description, self.amount, self.units)
