# Francesca Nguyen, fnguyen3@usc.edu
# ITP 115, Spring 2022
# Section: Ramen
# Final Project
# main_nguyen_francesca.py
# Description:
# The file runs the main function which tests the code/functions of tasks and interface files. The purpose of this program is to serve as a park dictionary for the user.

from tasks import *
from interface import *

# runs everything
def main():
    print("National Parks") # text at the top when running program
    parksList = readParksFile() # dictionary
    menu = getMenuDict() # pulls user menu
    choice = "" # placeholder
    while choice.upper() != "Q": # when user inputs q, program stops
        print()
        displayMenu() # displays the menu and its choices
        choice = getUserChoice(menu)
        if choice.upper() == "A": # when user inputs a, function below runs
            printAllParks(parksList)
        elif choice.upper() == "B": # when user inputs b, function below runs
            printParksInState(parksList)
        elif choice.upper() == "C": # when user inputs c, function below runs
            printLargestPark(parksList)
        elif choice.upper() == "D": # when user inputs d, function below runs
            printParksForSearch(parksList)

main()
