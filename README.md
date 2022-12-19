# Welcome to PyPet!

## Link to Source Control Repository

https://github.com/Tucky28/NatalieTucknott_T1A3.git

### Style Guide that code adheres to

PEP 8 – Style Guide for Python Code

### Features of PyPet

- User can create pet - pet type and pet name
- Menu items:

1. Feed pet
2. Play with Pet
3. Teach pet a new word
4. Bedtime for pet
5. Take pet for walk
6. Pet store
7. Inventory
8. Quit

- Pet can level up to level two and three
- Pet Store and Take pet for a walk unlock as the pet levels up
- Hunger, Sleep, Excitement and age decrease and increase depending on how the user interacts with the pet
- Pet Status to see how the pet is feeling
- Error messages if the pet variables are at maximum so the user cannot keep choosing the same option
- Age increases every 15 seconds and Hunger, Sleep and Excitement decrease
- Coins can be used in the store to purchase items for the pet
- Error messages if the user does not have enough coins
- Items purchased get moved to the inventory and removed from the available items in Pet Store
- When you take the pet for a walk, you can pick up a random amount of coins each time

### Implementation Plan

Use of Trello
https://trello.com/invite/b/Q4TzllNr/ATTI16bd9f266fbb6696e0c7e196451d3c8dD1295781/terminal-application-t1a3

### Help Documentation

Steps to install PyPet

1. Download the source code from my GitHub repositorry by clicking on 'code' in the right hand corner and 'Download zip'
2. Go to your terminal on your computer
3. Change directory to NatalieTucknott_T1A3
   - If you're unsure of how to do this copy this code into your terminal `cd NatalieTucknott_T1A3`
4. Move into the virtual environment (venv) by running the following code `source venv/bin/activate`
5. Run the following code in your terminal `./run_pypet.sh`

Now you can start playing PyPet!

#### Dependencies

1. Ensure you have the latest version of Python installed on your computer first. For instructions on how to do this, check out this link - https://www.codecademy.com/article/install-python3

#### Command Line Arguements

1. You will need to input a pet type and pet name. You can enter in any character but you cannot continue if nothing is entered.
2. The application will then ask you to choose a number from the provided options as you move through the rest of the app. Anything else inputted, will return an error.

### References

Python enhancement proposals (no date) PEP 8 – Style Guide for Python Code. Available at: https://peps.python.org/pep-0008/ (Accessed: December 19, 2022).
