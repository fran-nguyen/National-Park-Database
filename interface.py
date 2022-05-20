# Francesca Nguyen, fnguyen3@usc.edu
# ITP 115, Spring 2022
# Section: Ramen
# Final Project
# interface.py
# Description:
# This file will define functions that will be called from other functions in another Python file (main_nguyen_francesca.py)

from tasks import *

# function: getMenuDict
# parameter: none
# return value: a dictionary where the keys are letters for the user to input and the values are descriptions of the menu options
# menu
def getMenuDict():
    menuDict = {"A": "All national parks",
        "B": "Parks in a particular state",
        "C": "The largest park",
        "D": "Search for a park",
        "Q": "Quit"}
    return menuDict # menu with the choices

# function: displayMenu
# parameter: none
# return value: none
# displays what menu looks like to user
def displayMenu():
    dictionary = getMenuDict() # uses getMenuDict() for the dictionary
    for options in dictionary:
        print(options, "->", dictionary[options]) # prints the options out for user

# function: getUserChoice
# parameter: menuDict
# return value: a string that is a valid choice entered by the user
# get input from the user
def getUserChoice(menuDict):
    choice = input("Choice: ").upper() # user input and changes response to be all uppercase to match options
    while choice != "A" and choice != "B" and choice != "C" and choice != "D" and choice != "Q": # if none of these are picked, it will reask the input to user
        choice = input("Choice: ").upper() # asks for user input if none of the choices above were picked
    return choice

# function: printAllParks
# parameter: parksList
# return value: none
# prints parks
def printAllParks(parksList):
    # it showcases regular printing in the parkAllParks function
    for park in parksList: # runs through dictionary
        print(park["Name"] + " (" + park["Code"] + ")\n" + # prints name and code
            "\tLocation: " + park["State"] + "\n" + # prints location
            "\tArea: " + park["Acres"] + " acres\n" + # prints area/size
            "\tDate Established: " + convertDate(park["Date"])) # prints date

# function: getStateAbbr
# parameter: none
# return value: a string with a two-letter abbreviation of a state
# gets input from the user for a state
def getStateAbbr():
    state = input("Enter a state: ") # gets user input
    while len(state) != 2: # if user enters more or less than 2 letters, it will tell user to enter another state
        print("Need the two letter abbreviation") # prints clarification
        state = input("Enter a state: ")
    return state.upper() # returns the abbreviation in all uppercase to match state abbreviation norms

# function: printParksInState
# parameter: parksList
# return value: none
# loops through parks in list and prints info if state is found
def printParksInState(parksList):
    state = getStateAbbr() # gets the state from user input
    valid = False # loop
    for park in parksList: # goes through dictionary
        if park["State"] == state: # if it finds the abbreviation, it prints the state's parks and info
            print(park["Name"] + " (" + park["Code"] + ")\n" +
                "\tLocation: " + park["State"] + "\n" +
                "\tArea: " + park["Acres"] + " acres\n" +
                "\tDate Established: " + convertDate(park["Date"]))
            valid = True
    if not valid: # if no state is found or state is invalid, it will print to user that it does not exist
        print("There are no national parks in", state, "or it is not a valid state.") # prints and puts user input abbreviation in statement

# function: printLargestPark
# parameter: parksList
# return value: none
# prints the largest park
def printLargestPark(parksList):
    largeParkCode = getLargestPark(parksList) # calls function form tasks.py and finds the park with the largest area and becomes the value of largeParkCode
    for park in parksList: # runs though dictionary
        if park["Code"] == largeParkCode: # once it finds the biggest park, it prints the following info of the park
            print(
                park["Name"] + " (" + park["Code"] + ")\n" +
                "\tLocation: " + park["State"] + "\n" +
                "\tArea: " + park["Acres"] + " acres\n" +
                "\tDate Established: " + convertDate(park["Date"]) + "\n" +
                "\tDescription: " + park["Description"])
            return

# function: printParksForSearch
# parameter: parksList
# return value: none
# finds key word input from user to see if it applies to a park
def printParksForSearch(parksList):
    key = input("Enter test for searching: ") # user input to find whether a park hosts a key search term
    key = key.lower() # makes user input lowercase
    valid = False # loop
    for park in parksList: # goes through dictionary
        if key in park["Name"].lower() or key in park["Code"].lower() or key in park["Description"]: # checks if key word is in name, code, or description
            valid = True
            print(park["Name"] + " (" + park["Code"] + ")\n" + # if found, it'll print the list of parks with their info
                "\tLocation: " + park["State"] + "\n" +
                "\tArea: " + park["Acres"] + " acres\n" +
                "\tDate Established: " + convertDate(park["Date"]) + "\n" +
                "\tDescription: " + park["Description"])
            print() # spacer inbetween info sets
    if not valid: # if not found in name, code, or description
        print("There are no national parks for the search text of","'"+key+"'"+".") # prints statement to user with the input they provided