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
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        word = "Abacus"
        result = hw1.vowel_count(word)
        self.assertEqual(result,3)

    def test_vowel_count_empty_string(self):
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        word = ""
        result = hw1.vowel_count(word)
        self.assertEqual(result,0)
    
    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        # TODO: Arrange inputs, call hw1.short_lists, and assert the result.
        shortLists = [[1],[3,5],[],[6,42,3],[1,4]]
        result = hw1.short_lists(shortLists)
        self.assertEqual(result ,[[3,5],[1,4]])

    def test_short_lists_no_matching_lengths(self):
        # TODO: Arrange inputs, call hw1.short_lists, and assert the result.
        shortLists = [[],[3,4,2],[5]]
        result = hw1.short_lists(shortLists)
        self.assertEqual(result,[])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        # TODO: Arrange inputs, call hw1.ascending_pairs, and assert the result.
        listPairs = [[3,4],[1,2],[3,6],[4,4]]
        result = hw1.ascending_pairs(listPairs)
        self.assertEqual(result ,[[3,4],[1,2],[3,6],[4,4]])

    def test_ascending_pairs_other_lengths_unchanged(self):
        # TODO: Arrange inputs, call hw1.ascending_pairs, and assert the result.
        listPairs = [[6,3],[6,5,2],[9,2],[4,5,2]]
        result = hw1.ascending_pairs(listPairs)
        self.assertEqual(result ,[[3,6],[6,5,2],[2,9],[4,5,2]])

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
        first = data.Price(3,45)
        second = data.Price(2,45)
        result = hw1.add_prices(first,second)
        self.assertEqual(result,data.Price(5,90))

    def test_add_prices_with_cents_carry(self):
        # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
        first = data.Price(3,45)
        second = data.Price(2,65)
        result = hw1.add_prices(first,second)
        self.assertEqual(result,data.Price(6,10))


    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        point1 = data.Point(5,1)
        point2 = data.Point(2,5)
        twoPoints = data.Rectangle(point2, point1)
        result = hw1.rectangle_area(twoPoints)
        self.assertEqual(result,12)

    def test_rectangle_area_negative_coordinates(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        point1 = data.Point(-3,4)
        point2 = data.Point(2,-6)
        twoPoints = data.Rectangle(point1, point2)
        result = hw1.rectangle_area(twoPoints)
        self.assertEqual(result,50)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        shelf = [data.Book(["Gilbert Gotfried","Hayao Miyazaki"],"This Book Isn't Real"),data.Book(["J. R. R. Tolkien"],"Fellowship of The Ring"),data.Book(["Gilbert Gotfried"],"How To Be Uncreative"),data.Book(["AuthorGuy"],"I Dont Even Know"),data.Book(["Author McGee","Gilbert Gotfried"],"Im running out of names here")]
        result = hw1.books_by_author("Gilbert Gotfried", shelf)
        self.assertEqual(result, ["This Book Isn't Real", "How To Be Uncreative", "Im running out of names here"])

    def test_books_by_author_no_matches(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        shelf = [data.Book(["Gilbert Gotfried","Hayao Miyazaki"],"This Book Isn't Real"),data.Book(["J. R. R. Tolkien"],"Fellowship of The Ring"),data.Book(["Gilbert Gotfried"],"How To Be Uncreative"),data.Book(["AuthorGuy"],"I Dont Even Know"),data.Book(["Author McGee","Gilbert Gotfried"],"Im running out of names here")]
        result = hw1.books_by_author("oneGuy", shelf)
        self.assertEqual(result, [])
        

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        point1 = data.Point(2,4)
        point2 = data.Point(4,2)
        rectangleExample = data.Rectangle(point1, point2)
        result = hw1.circle_bound(rectangleExample)
        self.assertEqual(result.center,(3,3))
        self.assertAlmostEqual(result.radius, 1.4142135623)  

    def test_circle_bound_non_square_rectangle(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        self.fail("TODO: write the second unit test for circle_bound")

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        self.fail("TODO: write the first unit test for below_pay_average")

    def test_below_pay_average_empty_list(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        self.fail("TODO: write the second unit test for below_pay_average")


if __name__ == '__main__':
    unittest.main()
