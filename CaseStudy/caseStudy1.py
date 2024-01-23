# Food Ordering System

from array import array
import os
from art import text2art
from tabulate import tabulate

item_code = ['C01', 'C02', 'C03']
item_name = ['Burger', 'Fries', 'Sandwich']
price = [25.00, 45.00, 50.00]
orders = []

#function to display the menu
def display_menu():
    for i in range(len(item_code)):
        print(f"{item_code[i]}   {item_name[i]:10}   {price[i]:.2f}")

def display_header():
    header = text2art("McBee")
    print(header)

# function to clear screen
def clear_screen():
    os.system('cls')

# function to pause the screen
def press_key():
    input("Press any key to continue...")

if __name__ == '__main__':
    display_header()

    print("1. Display Menu")
    print("2. Place Order")
    print("3. View Order")
    print("4. Exit")
    choice = int(input("Please make a selection: "))


    if choice == 1:
        display_menu()
    elif choice == 2:
        #place_order()
        print()
    elif choice == 3:
        #view_order()
        print()
    elif choice ==4:
        print("Thank you for using McBee!")
        print("Exiting program...")
        exit
    else:
        print("Please enter a number from 1 to 4")
    display_menu()