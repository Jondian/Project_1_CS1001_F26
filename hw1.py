"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data
from math import sqrt

# Part 1: vowel_count
def vowel_count(text: str) -> int:
    vowelCounter = 0 #accumulator for vowels
    for i in text: #goes through the text letter by letter
        if i.lower() in ("a", "e", "i", "o", "u"): #checks if the letter is a vowel
            vowelCounter += 1 # if there is a vowel increase the counter by 1
    return vowelCounter # return the amount of values in the string 

    # Purpose: counts vowels in a given string
    # Input(s): text is a string given
    # Output: returns the amount of vowls in the text
    # Replace this exception with your implementation.
    raise NotImplementedError("Part 1: implement vowel_count")


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    actualShortList = []    # creates a new list for the passing nested lists to go to
    for i in items:     # goes through each nested list
        if len(i) == 2: # checks if the list has a length of 2 items
            actualShortList.append(i) # appends the list to the new variable
    return actualShortList # returns the lists that had a length of 2

    # Purpose: describe what this function computes.
    # Input(s): explain each parameter.
    # Output: explain what the function returns.
    # Replace this exception with your implementation.
    raise NotImplementedError("Part 2: implement short_lists")

# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # Purpose: creates a list of nested lists that do not have any list pairs in descending order
    # Input(s): list of nested lists.
    # Output: returns a list of nested pairs, with no pairs in descending order    

    newListPair = [] #new list for function to return
    for row in items: #checks the nested lists, AKA "rows"
        if len(row) == 2 and row[0] > row[1]: #checks if the list is a pair and is descending
            tempList = [row[1],row[0]] # changes the descending pair into a non-descending pair
            newListPair.append(tempList) # appends the non-descending pair to new List
        else: #  if the list length isnt equal to 2 or the pair is non-descending
            newListPair.append(row) # appends list to the new list
    return newListPair # returns the new list

        

    raise NotImplementedError("Part 3:implement ascending_pairs")


# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # Purpose: adds prices of two price objects
    # Input(s): first and second are price objects with dollar and cent amounts
    # Output: adds both dollars and cent amounts from both objects, while also adding a dollar if cent is greater than 100
    # Replace this exception with your implementation.    
    totalDollar = first.dollars + second.dollars #adds the dollar amount of the first and second price objects
    totalCents = first.cents + second.cents #adds cent ammount for the first and second price object
    if totalCents >= 100: #checks if the total cents is greater than 100
        totalCents -= 100 #if it passes, it goes down 100 cents
        totalDollar += 1 #adds dollar to total price
    return data.Price(totalDollar,totalCents) #returns a new price object, representing the total price in dollars and cents



    raise NotImplementedError("Part 4: implement add_prices")


# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # Purpose: calculates area of a rectangle
    # Input(s): Rectangle class with 2 points, representing top left corner and bottom right corner
    # Output: returns the area of the rectangle based on the two points
    # Replace this exception with your implementation.  
  
    height = rectangle.top_left.y - rectangle.bottom_right.y
    width = rectangle.bottom_right.x - rectangle.top_left.x
    return sqrt((height * width) ** 2 )

    raise NotImplementedError("Part 5: implement rectangle_area")


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # Purpose: computes and creates a list of books by a chosen author
    # Input(s): a list of book objects
    # Output: returns a list of books that were created by a chosen author
    # Replace this exception with your implementation.    
    bookList = []
    for i in books:
        for authorName in i.authors:
            if authorName == author:
                bookList.append(i.title)
    return bookList
                

    raise NotImplementedError("Part 6: implement books_by_author")


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # Purpose: calculates the center and radius of a circle that represents the smallest circle enclosing the rectangle
    # Input(s): a rectangle class
    # Output: returns and creates a circle class that has the coordinates (x,y) of the center of the rectangle, and the radius of the circle based on the distance between the corners divided by 2
    # Replace this exception with your implementation.    
    
    rectangleCenterX = rectangle.top_left.x + ((rectangle.bottom_right.x - rectangle.top_left.x)/2)
    rectangleCenterY = rectangle.bottom_right.y + ((rectangle.top_left.y - rectangle.bottom_right.y)/2)
    diameter = sqrt(((rectangle.bottom_right.x - rectangle.top_left.x)**2) + ((rectangle.bottom_right.y - rectangle.top_left.y)**2))

    return data.Circle((rectangleCenterX, rectangleCenterY), diameter/2)

    raise NotImplementedError("Part 7: implement circle_bound")

# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # Purpose: computes the average pay rate across all employees and lists the names of employees under that average
    # Input(s): employees: a list of employee classes and their attributes
    # Output: returns a list that shows which employee is under the pay average of all employees
    # Replace this exception with your implementation.    
    
    if len(employees) == 0:
        return None
    total = 0
    employeeList = []
    for employee in employees:
        total += employee.pay_rate
    average = total/len(employees)
    for employee in employees:
        if employee.pay_rate < average:
            employeeList.append(employee.name)
    return employeeList


    raise NotImplementedError("Part 8: implement below_pay_average")
