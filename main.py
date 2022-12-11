import datetime
import time
from random import randrange
import pickle
import threading

PERIOD_SEC = 10

# Created pet class with variables for all pets
class Pet(object):
    name = [""]
    pet_type = [""]
    age = 0
    excitement_reduce = 2
    excitement_max = 10
    excitement_warning = 3
    food_reduce = 2
    food_max = 10
    food_warning = 2
    level = 0
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
        self.name = name
        self.pet_type = pet_type
        self.sleep = randrange(self.sleep_max)
        self.vocab = self.vocab[:]

    # to start your timer
    def make_alive(self):
        self.timer_task = threading.Timer(PERIOD_SEC, self.__clock_tick)
        self.timer_task.start()

    # to stop your timer
    def kill(self):
        self.timer_task.cancel()

     # Function created to reduce variables
    def __clock_tick(self):
        self.food -= 1
        self.sleep -= 1
        self.excitement -=1
        self.age += 2
        
    
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
        self.vocab.append(new_word)
        self.food -= self.food_reduce
        self.sleep -= self.sleep_reduce

    # Feed pet and increase food variable
    # Print the status of the pet
    def feed(self):
        print("***CRUNCH*** mmm.. Thank you!")
        print(self.status())
        meal = randrange(1,5)
        self.food += meal

        if self.food < 0:
            self.food = 0
            print ("I'm still ", self.mood)
        else:
            self.food > self.food_max
            self.food = self.food_max
            print("***BURP*** I'm so full")
    
    # Play with pet and increase excitement
    # Print the status of the pet
    def play(self):
        print("WOOHOO!")
        print(self.status())
        fun = randrange(1,5)
        self.excitement += fun
        self.sleep -= self.sleep_reduce
        self.food -= self.sleep_reduce

        if self.excitement < 0:
            self.excitement = 0
            print ("I'm still ", self.mood())
        else: 
            self.excitement > self.excitement_max
            self.excitement = self.excitement_max
            print("I'm having SO MUCH FUN!")

    # Print status of pets food, sleep and excitement
    def status(self):
        print("I\'m ", self.mood())
        print("Hunger level", self.food)
        print("Sleep level ", self.sleep)
        print("Excitement level " , self.excitement)
        print("Age is " , self.age) 

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
        print("5 - Quit")  

    print("Hello I am", my_pet.name, "and I'm a", my_pet.pet_type, "!")
    print(my_pet.status())
    print_menu()
        
    while True:
        option = int(input())
        if option == 1:
            my_pet.feed()
        elif option == 2:
            my_pet.play()
        elif option == 3:
            my_pet.teach()
        elif option == 4:
            print("In progress..")
        elif option == 5:
            print("Quitting in progress..")
        else:
            print("Bye")
            break

        print_menu()
        
main()
