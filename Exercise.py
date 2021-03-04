import random


class Exercise:
    def __init__(self, desc, type, logger):
        self.description = desc
        self.type = type
        self.logger = logger
        self.amount = self.get_amount()

    def get_amount(self):
        hard_possible_amounts = ['2', '6', '10']
        medium_possible_amounts = ['6', '10', '16']
        easy_possible_amounts = ['10', '16', '20']
        machine_possible_amounts = ['20 kcal', '30 kcal']
        calisthenics_possible_amounts = ['20 sec', '30 sec']
        cardio_possible_amounts = ['25', '50']

        try:
            if self.type == 'Hard':
                return random.choice(hard_possible_amounts)
            elif self.type == 'Medium':
                return random.choice(medium_possible_amounts)
            elif self.type == 'Easy':
                return random.choice(easy_possible_amounts)
            elif self.type == 'Machine':
                return random.choice(machine_possible_amounts)
            elif self.type == 'Calisthenics':
                return random.choice(calisthenics_possible_amounts)
            else:
                return random.choice(cardio_possible_amounts)

        except:
            self.logger.error('an exception occurred')

    def print(self):
        return '{} {}'.format(self.amount, self.description)
