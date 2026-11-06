"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data


# Part 1: vowel_count
def vowel_count(text: str) -> int:
    vowelCounter = 0 #accumulator for vowels
    for i in text: #goes through the text letter by letter
        if i.lower() in ("a", "e", "i", "o", "u"): #checks if the letter is a vowel
            vowelCounter += 1 # if there is a vowel increase the counter by 1
    return vowelCounter # return the amount of values in the string 

    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 1: implement vowel_count")


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    actualShortList = []    #creates a new list for the passing nested lists to go to
    for i in items:     # goes through each nested list
        if len(i) == 2: # checks if the list has a length of 2 items
            actualShortList.append(i) # appends the list to the new variable
    return actualShortList # returns the lists that had a length of 2

    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 2: implement short_lists")

# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    newListPair = [] #new list for function to return
    for row in items: #checks the nested lists, AKA "rows"
        if len(row) == 2 and row[0] > row[1]: #checks if the list is a pair and is descending
            tempList = [row[1],row[0]] # changes the descending pair into a non-descending pair
            newListPair.append(tempList) # appends the non-descending pair to new List
        else: #  if the list length isnt equal to 2 or the pair is non-descending
            newListPair.append(row) # appends list to the new list
    return newListPair # returns the new list

        
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 3:implement ascending_pairs")


# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    totalDollar = first.dollars + second.dollars
    totalCents = first.cents + second.cents
    if totalCents >= 100:
        totalCents -= 100
        totalDollar += 1
    return data.Price(totalDollar,totalCents)


    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 4: implement add_prices")


# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    return rectangle.bottom_right * rectangle.top_left
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 5: implement rectangle_area")


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 6: implement books_by_author")


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 7: implement circle_bound")


# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 8: implement below_pay_average")
