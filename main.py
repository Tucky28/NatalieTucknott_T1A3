import time
from random import randrange
import threading
import sys
import shop

PERIOD_SEC = 15

# Created pet class with variables for all pets
class Pet(object):
    name = []
    pet_type = []
    age = 0
    coin = 0
    coin_min = 0
    coin_max = 100
    excitement_reduce = 2
    excitement_min = 0
    excitement_max = 10
    excitement_warning = 3
    food_min = 0
    food_reduce = 2
    food_max = 10
    food_warning = 2
    level = 1
    level_two = 2
    level_three = 3
    sleep_reduce = 1
    sleep_min = 0
    sleep_max = 10
    sleep_warning = 1
    vocab = []
    inventory = []

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
        self.inventory = self.inventory

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

    # Pet level up to two from one
    def pet_level(self):
        vocab_list = len(self.vocab)
        while self.level >= 2:
            break
        else:
            if vocab_list == 3:
                self.level += 1
                print("\n",self.name,"just leveled up!",self.name,"is now level",self.level,"")
                print("YOU UNLOCKED A NEW MENU ITEM - Take",self.name,"for a walk")

    # Pet level up to three from two
    def pet_level_two(self):
        while self.level >= 3:
            break
        else:
            if self.level == 2 and self.coin >= 3:
                self.level += 1
                print("\n",self.name,"just leveled up!",self.name,"is now level",self.level,"")
                print("YOU UNLOCKED A NEW MENU ITEM - Pet Store")

    # Teach pet new word and add to vocab
    def teach(self, new_word):
        new_word = input("What new word would you like to teach?")
        if new_word == "":
            print("Oops! You need to enter a word to continue")
        else:
            print("\nThanks for teaching me how to say",new_word,"!")
            self.vocab.append(new_word)
            print("I've learnt how to say:", *self.vocab,sep='\n')
            self.food -= self.food_reduce
            self.sleep -= self.sleep_reduce
            self.min_max_level()

    # Feed pet and increase food variable
    def feed(self):
            print("***CRUNCH*** mmm.. Thank you!")
            meal = randrange(1,5)
            self.food += meal
            self.sleep -= self.sleep_reduce
            self.min_max_level()

    # Play with pet and increase excitement
    def play(self):
        print('WOOHOOO!')
        fun = randrange(1,5)
        self.min_max_level()
        self.excitement += fun
        self.sleep -= self.sleep_reduce
        self.food -= self.food_reduce
   
    # Take pet for a walk and pick up coins
    # Print the coins collected on walk
    def walk(self):
            print("Walk in progress...")
            time.sleep(1)
            self.min_max_level()
            self.excitement += 3
            self.sleep -= self.sleep_reduce
            self.food -= self.food_reduce
            coins = randrange(0,7)
            self.coin += coins
            print("What an adventure!",self.name, "picked up",coins, "coins" )
            print(self.name, "now has",self.coin,"coins")

    # Take pet to bed
    def bedtime(self):
            print('***YAWN***')
            time.sleep(1)
            print('zzz...')
            time.sleep(1)
            self.min_max_level()
            sleep = randrange (1,5)
            self.sleep += sleep
            self.food -= self.food_reduce
            self.excitement -= self.excitement_reduce

    # Print status of pets food, sleep and excitement
    def status(self):
        time.sleep(1)
        print("+---------------------+")
        print(" PET STATUS:","I'm",self.mood(),"\n")
        print(" Hunger:",self.food)
        print(" Sleep:",self.sleep)
        print(" Excitement:",self.excitement)
        print(" Age:" ,self.age) 
        self.pet_level_two()
        self.pet_level()
        print("+---------------------+")
        return ""

 # Max and min range for pet variables
    def min_max_level(self):
        self.food = min(max(self.food_min, self.food), self.food_max)
        self.sleep = min(max(self.sleep_min, self.sleep), self.sleep_max)
        self.excitement = min(max(self.excitement_min, self.excitement), self.excitement_max)
        self.coin = min(max(self.coin_min, self.coin), self.coin_max)

 # Go to pet store, purchase items and add to inventory
    def pet_store_items(self):
        print("+---------------------------+")
        print("| Welcome to the Pet Store! |")
        print("+---------------------------+")
        if shop.shop.store_items == {}:
            print("No items available for sale - You've bought everything!")
        else:
            print("\nItems available to buy:")
            for key, value in shop.shop.store_items.items():
                print(key, ' : ', value)
            print("\n0 - Go back home")
        
        while True:
            choice = input()
            if choice == '1' and self.coin <= 2:
                print("You don't have enough coins to purchase this item\n")
            elif choice == '1' and self.coin >= 2:
                self.coin -= 3
                shop.shop.store_items.pop('1 - Squeezy Ball Toy', 2)
                self.inventory.append('Squeezy Ball Toy')

            elif choice == '2' and self.coin <= 5:
                print("You don't have enough coins to purchase this item\n")
            elif choice == '2' and self.coin >= 5:
                self.coin -= 6
                shop.shop.store_items.pop('2 - Snooze 2000 Pet Bed', 5)
                self.inventory.append('Snooze 2000 Pet Bed')
            
            elif choice == '3' and self.coin <= 10:
                print("You don't have enough coins to purchase this item\n")
            elif choice == '3' and self.coin >= 10:
                self.coin -= 8
                shop.shop.store_items.pop('3 - Xtra Nutrient Pet Food', 10)
                self.inventory.append('Xtra Nutrient Pet Food')

            elif choice == '0':
                break
            else:
                print("Oops! That's an invalid option")
            
            print("You have the following items in your inventory:", *self.inventory,sep='\n')
            if shop.shop.store_items == {}:
                print("No items available for sale - You've bought everything!")
            else:
                print("\nItems available to buy:")
                for key, value in shop.shop.store_items.items():
                    print(key, ' : ', value)
            print("\n0 - Go back home")

    # Inventory for pets items to be stored in
    def inventory_menu(self):
        print("Inventory contains:")
        if self.inventory == []:
            print("You haven't purchased anything yet from the Pet Store for",self.name)
        else:
            print(*self.inventory,sep='\n')
        print(self.name,"has collected",self.coin, "coins")

          
# Created main for user to create pet and interact
def main():
    print('+---------------------+')
    print("|  Welcome to PyPet!  |")
    print('+---------------------+')
    while True:
        pet_type = input("Let's begin!\n\nWhat type of animal is your pet?\nAnimal Type: ")
        if pet_type != '':
            break

    while True:
        pet_name = input("\nWhat would you like to name your pet? ")
        if pet_name != '':
            break
    # Create new pet
    my_pet = Pet(pet_name, pet_type)
    my_pet.make_alive()

    # Unique menu options depending on the level of the pet 
    def print_menu():
        if my_pet.level == 1:
            print("\nInteract with",my_pet.name,":")
            print("1 - Feed", my_pet.name)
            print("2 - Play with", my_pet.name)
            print("3 - Teach", my_pet.name, "a new word")
            print("4 - Bedtime for", my_pet.name)
            print("7 - Inventory")
            print("0 - Quit\n") 
        elif my_pet.level == 2:
            print("\nInteract with",my_pet.name,":")
            print("1 - Feed", my_pet.name)
            print("2 - Play with", my_pet.name)
            print("3 - Teach", my_pet.name, "a new word")
            print("4 - Bedtime for", my_pet.name)
            print("5 - Take", my_pet.name, "for a walk")
            print("7 - Inventory")
            print("0 - Quit\n")
        elif my_pet.level == 3:
            print("\nInteract with",my_pet.name,":")
            print("1 - Feed", my_pet.name)
            print("2 - Play with", my_pet.name)
            print("3 - Teach", my_pet.name, "a new word")
            print("4 - Bedtime for", my_pet.name)
            print("5 - Take", my_pet.name, "for a walk")
            print("6 - Pet Store")
            print("7 - Inventory")
            print("0 - Quit\n")  
    
    print("\n--- Hello! ---\n I am", my_pet.name, "and I'm a",my_pet.pet_type,"!")
    print(my_pet.status())
    time.sleep(1)
    print_menu()

    # Menu selections and error messages
    while True:
        option = input()
        if option == '1':
            if my_pet.food >= my_pet.food_max:
                print("I'm too full to eat")
            else:
                my_pet.feed()
        elif option == '2':
            if my_pet.excitement >= my_pet.excitement_max:
                print("I'm too excited to play again")
            else:
                my_pet.play()
        elif option == '3':
            my_pet.teach(new_word='')
        elif option == '4':
            if my_pet.sleep >= my_pet.sleep_max:
                print("I'm not tired'")
            else:
                my_pet.bedtime()
        elif option == '5':
            if my_pet.level == 1:
                print("Oops! That's an invalid option")
            elif my_pet.excitement >= my_pet.excitement_max:
                print("I'm too excited to play again")
            else:
                my_pet.walk()
        elif option == '6':
            if my_pet.level <= 2:
                print("Oops! That's an invalid option")
            else:
                my_pet.pet_store_items()
        elif option == '7':
            my_pet.inventory_menu()
        elif option == '0':
            print("See you next time..")
            sys.exit()
        else:
            print("Oops! That's an invalid option")
        my_pet.min_max_level()
        my_pet.status()
        print_menu()

if __name__ == '__main__':
    main()