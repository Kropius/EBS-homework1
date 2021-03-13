import math
from data_generator import *


class GenerateSubscriptions:

    field_occurrences = dict()
    subscriptions = []

    def __init__(self, total_number_of_subscriptions, field_frequencies):
        self.total_number_of_subscriptions = total_number_of_subscriptions
        self.field_frequencies = field_frequencies
        self.calculate_field_occurences()

    def calculate_field_occurences(self):
        for key in self.field_frequencies:
            key_occurrences = (self.field_frequencies[key]/100) * self.total_number_of_subscriptions
            self.field_occurrences[key] = math.floor(key_occurrences)

    def generate_value(self, key_name):
        if key_name == 'wind_direction':
            return generate_directions(1)[0]
        elif key_name == 'city':
            return generate_cities(1)[0]
        elif key_name == 'temp':
            return generate_temperatures(1)[0]

    def generate_subscriptions(self):
        operator_possibilities = ['=', '>', '<', '>=', '<=']
        remaining_subscriptions = self.total_number_of_subscriptions
        for index in range(self.total_number_of_subscriptions):
            subscription = []
            for key in self.field_occurrences:
                coin = random.choice([0, 1])
                if self.field_occurrences[key] == remaining_subscriptions or (coin == 1 and self.field_occurrences[key] > 0):
                    field = list()
                    field.append(key)
                    if key == 'city' or key == 'direction':
                        field.append('=')
                    else:
                        field.append(random.choice(operator_possibilities))
                    field.append(self.generate_value(key))
                    subscription.append(tuple(field))
                    self.field_occurrences[key] -= 1
            print(subscription)
            remaining_subscriptions -= 1
