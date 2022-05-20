# Francesca Nguyen, fnguyen3@usc.edu
# ITP 115, Spring 2022
# Section: Ramen
# Final Project
# tasks.py
# Description:
# This file defines functions that will be called from other functions in another Python file (interface.py)

# function: readParksFile
# parameter: fileName
# return value: a list of parks
# dictionary of parks from csv
def readParksFile(fileName='national_parks.csv'):
    readFile = open(fileName, "r") # opens file
    parksList = [] # empty list to hold dictionary
    head = readFile.readline().split(",") # splits the info by using the , in the data set for each header
    for i in range(0, 56): # there are 56 rows of parks
        park = {} # hold parks
        line = readFile.readline()
        description = line.split("\"")[1] # splits with \ rather than , because we want to include the whole description (which has commas in it)
        park[head[7].strip()] = description # separates the 7th heading which is the description
        data = line.split(",")[0:7] # gets all the data inbetween headers 0-6, 7 is not included due to it being the description
        for x in range(0,7):
            park[head[x]] = data[x] # adds respective description to the park data
        parksList.append(park) # adds data to the dictionary
    return parksList

# function: convertDate
# parameter: dataStr
# return value: a string with the date in the following format: Month Day, Year
# turns numerical date to standard date
def convertDate(dataStr):
    monthName = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    time = dataStr.split("-") # splits the date's numbers
    year = time[0] # correlates to the first
    month = int(time[1]) # correlates to the second
    day = time[2] # correlates to the third
    date = monthName[month-1]+" "+day+ ", "+year # january = 0, so if month was 1, you'd have to subtract 1 to get 0
    return date

# function: getLargestPark
# parameter: parksList
# return value:  a string that is the park code of the park with the largest area
# gets largest park
def getLargestPark(parksList):
    code = "" # empty string to hold code
    max = 0 # will get updated later
    for park in parksList: # goes through dictionary
        size = int(park["Acres"]) # loops through to replace size with each of the park's size
        if size>max: # will continuously update to find the largest park
            max = size
            code = park["Code"] # makes the largest park the code
    return code