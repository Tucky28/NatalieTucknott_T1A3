import datetime
import time
from random import randrange
import pickle
import threading
import sys

PERIOD_SEC = 10

# Created pet class with variables for all pets
class Pet(object):
    name = []
    pet_type = []
    age = 0
    coin = 0
    excitement_reduce = 2
    excitement_min = 0
    excitement_max = 10
    excitement_warning = 3
    food_min = 0
    food_reduce = 2
    food_max = 10
    food_warning = 2
    level = 0
    sleep_reduce = 1
    sleep_min = 0
    sleep_max = 10
    sleep_warning = 1
    vocab = []

    # Created constructor for pet
    def __init__(self, name, pet_type):
        self.age = self.age
        self.excitement = randrange(self.excitement_max)
        self.food = randrange(self.food_min, self.food_max)
        self.level = self.level
        self.name = name
        self.pet_type = pet_type
        self.sleep = randrange(self.sleep_max)
        self.vocab = self.vocab
        self.coin = self.coin

     # Function created to reduce all variables
    def __clock_tick(self):
        self.make_alive()
        self.min_max_level()
        self.food -= 1
        self.sleep -= 1
        self.excitement -=1
        self.age += 2
    
    # to start timer
    def make_alive(self):
        self.timer_task = threading.Timer(PERIOD_SEC, self.__clock_tick)
        self.timer_task.start()

    # to stop timer
    def kill(self):
        self.timer_task.cancel()
    
    # Set the status of the pets mood
    def mood(self):
        if self.excitement <= self.excitement_warning and self.sleep <= self.sleep_warning and self.food <= self.food_warning:
            return 'Dying please help!'
        elif self.food <= self.food_warning and self.excitement <= self.excitement_warning:
            return 'Hungry and Bored'
        elif self.food <= self.food_warning and self.sleep <= self.sleep_warning:
            return 'Hungry and Sleepy'
        elif self.excitement <= self.excitement_warning and self.sleep <= self.sleep_warning:
            return 'Sleepy and Bored'
        elif self.food <= self.food_warning:
            return 'Hungry'
        elif self.excitement <= self.excitement_warning:
            return 'Bored'
        elif self.sleep <= self.sleep_warning:
            return 'Sleepy'
        else:
            return 'Happy'

    # Teach pet new word and add to vocab + decrease mood
    def teach(self, new_word):
        new_word = input("What new word would you like to teach?")
        self.vocab.append(new_word)
        self.food -= self.food_reduce
        self.sleep -= self.sleep_reduce
        self.min_max_level()
        self.pet_level()

    def pet_level(self):
        vocab_list = len(self.vocab)
        if vocab_list == 2:
            self.level += 1
            print(self.name,"just leveled up!")
            print(self.name, "is now level",self.level)


    # Feed pet and increase food variable
    # Print the status of the pet
    def feed(self):
        print("***CRUNCH*** mmm.. Thank you!")
        meal = randrange(1,5)
        self.food += meal
        self.sleep -= self.sleep_reduce
        self.min_max_level()

    # Play with pet and increase excitement
    # Print the status of the pet
    def play(self):
        print('WOOHOOO!')
        fun = randrange(1,5)
        self.excitement += fun
        self.sleep -= self.sleep_reduce
        self.food -= self.food_reduce
        self.min_max_level()

    def walk(self):
        print("Walk in progress...")
        time.sleep(2)
        self.min_max_level()
        self.excitement += 1
        self.sleep -= self.sleep_reduce
        self.food -= self.food_reduce
        coins = randrange(0,5)
        self.coin += coins
        print("What an adventure!",self.name, "picked up",coins, "coins" )
        print(self.name, "now has",self.coin,"coins")


    def bedtime(self):
        print('***YAWN***')
        time.sleep(2)
        print('zzz...')
        time.sleep(2)
        sleep = randrange (1,5)
        self.min_max_level()
        self.sleep += sleep
        self.food -= self.food_reduce
        self.excitement -= self.excitement_reduce

    # Print status of pets food, sleep and excitement
    def status(self):
        print("Hunger level", self.food)
        print("Sleep level", self.sleep)
        print("Excitement level" , self.excitement)
        print("Age is" , self.age) 
        print("I\'m", self.mood())
        return

 # Max and min range for pet variables
    def min_max_level(self):
        self.food = min(max(self.food_min, self.food), self.food_max)
        self.sleep = min(max(self.sleep_min, self.sleep), self.sleep_max)
        self.excitement = min(max(self.excitement_min, self.excitement), self.excitement_max)

# Created main for user to create pet and print pet details
def main():
    pet_type = input("What type of animal is your pet? ")
    pet_name = input("What do you want to name your pet? ")

    # Create new pet
    my_pet = Pet(pet_name, pet_type)
    my_pet.make_alive()


    def print_menu():
        print("1 - Feed", my_pet.name)
        print("2 - Play with", my_pet.name)
        print("3 - Teach", my_pet.name, "a new word")
        print("4 - Bedtime for", my_pet.name)
        print("5 - Take", my_pet.name, "for a walk")
        print("6 - Quit")  

    print("Hello I am", my_pet.name, "and I'm a", my_pet.pet_type, "!")
    print(my_pet.status())
    print_menu()
        
    while True:
        option = input()
        if option == '1':
            my_pet.feed()
        elif option == '2':
            my_pet.play()
        elif option == '3':
            my_pet.teach(new_word='')
        elif option == '4':
            my_pet.bedtime()
        elif option == '5':
            my_pet.walk()
        elif option == '6':
            print("See you next time..")
            sys.exit()
        else:
            print("Oops! That's an invalid option")
        my_pet.min_max_level()
        my_pet.status()
        print_menu()


main()