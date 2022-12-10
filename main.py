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
    sleep_warning = 1
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
    
    # Function created to reduce variables
    def __clock_tick(self):
        self.food -= 1
        self.sleep -= 1
        self.excitement -=1

    # Set the status of the pets mood
    def mood(self):
        if self.food <= self.food_warning:
            return 'Hungry'
        elif self.excitement <= self.excitement_warning:
            return 'Bored'
        elif self.sleep <= self.sleep_warning:
            return 'Sleepy'
        elif (self.food <= self.food_warning) and (self.excitement <= self.excitement_warning):
            return 'Hungry and Bored'
        elif (self.food <= self.food_warning) and (self.sleep <= self.sleep_warning):
            return 'Hungry and Sleepy'
        elif (self.excitement <= self.excitment_warning) and (self.sleep <= self.sleep_warning):
            return 'Sleepy and Bored'
        elif (self.excitement <= self.excitment_warning) and (self.sleep <= self.sleep_warning) and (self.food <= self.food_warning):
            return 'Dying please help!'
        else:
            return 'Happy'

    # Teach pet new word and add to vocab + decrease mood
    def teach(self, new_word):
        self.vocab.append(new_word)
        self.__clock_tick

    # Feed pet and increase food variable
    # Print the status of the pet
    def feed(self):
        print("***CRUNCH*** mmm.. Thank you!")
        print(self.status)
        meal = randrange(self.food, self.food_max)
        self.food += meal

        if self.food < 0:
            self.food = 0
            print ("I'm still ", self.mood)
        elif self.food > self.food_max:
            self.food = self.food_max
            print("***BURP*** I'm so full")
    




        
