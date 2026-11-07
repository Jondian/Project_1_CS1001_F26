"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        # 
        word = "Abacus" # word input
        result = hw1.vowel_count(word) # makes the result value the return value of the function
        self.assertEqual(result,3) # checks if equal

    def test_vowel_count_empty_string(self):
        # Arrange inputs, call hw1.vowel_count, and assert the result.
        word = ""# word input
        result = hw1.vowel_count(word) # makes the result value the return value of the function
        self.assertEqual(result,0) # checks if equal
    
    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        # Arrange inputs, call hw1.short_lists, and assert the result.
        shortLists = [[1],[3,5],[],[6,42,3],[1,4]]
        result = hw1.short_lists(shortLists) # checks if the nested lists have a length = 2 and returns it into a new list
        self.assertEqual(result ,[[3,5],[1,4]])  # checks if it works

    def test_short_lists_no_matching_lengths(self):
        # Arrange inputs, call hw1.short_lists, and assert the result.
        shortLists = [[],[3,4,2],[5]] # contains no nested list that have a length of 2
        result = hw1.short_lists(shortLists) # checks if the nested lists have a length = 2 and returns it into a new list
        self.assertEqual(result,[]) # checks if it works, should return an empty list

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        # Arrange inputs, call hw1.ascending_pairs, and assert the result.
        listPairs = [[3,4],[1,2],[3,6],[4,4]]  # list of nested pair
        result = hw1.ascending_pairs(listPairs) # checks if pairs are ascending and returns changed list
        self.assertEqual(result ,[[3,4],[1,2],[3,6],[4,4]])  # no change

    def test_ascending_pairs_other_lengths_unchanged(self):
        # Arrange inputs, call hw1.ascending_pairs, and assert the result.
        listPairs = [[6,3],[6,5,2],[9,2],[4,5,2]] # list of nested lists, some with lengths greater than 2
        result = hw1.ascending_pairs(listPairs) # calls function, reversed any descending pair into non-descending pair
        self.assertEqual(result ,[[3,6],[6,5,2],[2,9],[4,5,2]]) # checks if is changes

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        # Arrange inputs, call hw1.add_prices, and assert the result.
        first = data.Price(3,45) #input 1
        second = data.Price(2,45) #input 2
        result = hw1.add_prices(first,second) # adds dollar and cents from both inputs together
        self.assertEqual(result,data.Price(5,90)) # checks if it returns a new price object

    def test_add_prices_with_cents_carry(self):
        # Arrange inputs, call hw1.add_prices, and assert the result.
        first = data.Price(3,45) # input 1
        second = data.Price(2,65) #input 2 
        result = hw1.add_prices(first,second) # adds both, if cents > 100, it removes 100 and adds 1 to dollar
        self.assertEqual(result,data.Price(6,10)) # checks if its matching


    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        # creates 2 points and uses those points to create an object, then calculates the area based of the two points.
        point1 = data.Point(5,1)
        point2 = data.Point(2,5)
        twoPoints = data.Rectangle(point2, point1)
        result = hw1.rectangle_area(twoPoints)
        self.assertEqual(result,12)

    def test_rectangle_area_negative_coordinates(self):
        # creates 2 points with a negative integer and uses those points to create an object, then calculates the area based of the two points.
        # should return a positive interger
        point1 = data.Point(-3,4)
        point2 = data.Point(2,-6)
        twoPoints = data.Rectangle(point1, point2)
        result = hw1.rectangle_area(twoPoints)
        self.assertEqual(result,50)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        # creates a list of book objects, checks for books by Gilbert Gotfried, returns 3 books
        shelf = [data.Book(["Gilbert Gotfried","Hayao Miyazaki"],"This Book Isn't Real"),data.Book(["J. R. R. Tolkien"],"Fellowship of The Ring"),data.Book(["Gilbert Gotfried"],"How To Be Uncreative"),data.Book(["AuthorGuy"],"I Dont Even Know"),data.Book(["Author McGee","Gilbert Gotfried"],"Im running out of names here")]
        result = hw1.books_by_author("Gilbert Gotfried", shelf)
        self.assertEqual(result, ["This Book Isn't Real", "How To Be Uncreative", "Im running out of names here"])

    def test_books_by_author_no_matches(self):
        # creates a list full of book objects, checks for author, Should return nothing
        shelf = [data.Book(["Gilbert Gotfried","Hayao Miyazaki"],"This Book Isn't Real"),data.Book(["J. R. R. Tolkien"],"Fellowship of The Ring"),data.Book(["Gilbert Gotfried"],"How To Be Uncreative"),data.Book(["AuthorGuy"],"I Dont Even Know"),data.Book(["Author McGee","Gilbert Gotfried"],"Im running out of names here")]
        result = hw1.books_by_author("oneGuy", shelf) 
        self.assertEqual(result, [])
        

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        # Creates 2 points, creates a square rectangle from those points, and calculates the radius and center of circle that can go around the rectangle
        point1 = data.Point(2,4)
        point2 = data.Point(4,2)
        rectangleExample = data.Rectangle(point1, point2)
        result = hw1.circle_bound(rectangleExample)
        self.assertEqual(result.center,(3,3))
        self.assertAlmostEqual(result.radius, 1.4142135623)  

    def test_circle_bound_non_square_rectangle(self):
        # Creates 2 points, creates a non - square rectangle from those points, and calculates the radius and center of circle that can go around the rectangle
        point1 = data.Point(3,4)
        point2 = data.Point(7,2)
        rectangleExample = data.Rectangle(point1, point2)
        result = hw1.circle_bound(rectangleExample)
        self.assertEqual(result.center,(5,3))
        self.assertAlmostEqual(result.radius, 2.2360679775)

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        # creates a list of employees with names and pay roll, call hw1.below_pay_average, and creates a list of people under the average payroll, which is chell.
        employee_list = [data.Employee("Harold", 5), data.Employee("Linda",5 ), data.Employee("Chell", 4), data.Employee("Terry", 5)]
        result = hw1.below_pay_average(employee_list)
        self.assertEqual(result,["Chell"])

    def test_below_pay_average_empty_list(self):
        # creates an empty list, call hw1.below_pay_average, and assert the result, being an empty list.
        employee_list = []
        result = hw1.below_pay_average(employee_list)
        self.assertEqual(result,None)


if __name__ == '__main__':
    unittest.main()
