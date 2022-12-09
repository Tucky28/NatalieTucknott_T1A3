import datetime
from random import randrange
import pickle

# Created pet class with variables for all pets
class pet(object):
    age: 0
    excitement_reduce = 3
    excitement_max = 10
    excitement_warning = 3
    food_reduce = 2
    food_max = 10
    food_warning = 2
    level: 0
    sleep_reduce = 1
    sleep_max = 10
    vocab = [""]

    # Created constructor for pet
    def __init__(self, name, pet_type):
        self.age = self.age
        self.excitement = randrange(self.excitement_max)
        self.food = randrange(self.food_max)
        self.level = self.level
        self.name = self.name
        self.pet_type = self.pet_type
        self.sleep = randrange(self.sleep_max)
        self.vocab = self.vocab[:]
        



