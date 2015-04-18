__author__ = 'Q'

import unittest
import random
from list_linked_e import List
import linked_sorts


class LinkedSortTests(unittest.TestCase):
    def setUp(self):
        self.tests = []
        basic_tests = [
            ([], []),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([3, 2, 1], [1, 2, 3]),
            ([5, 9, 1, 6], [1, 5, 6, 9]),
            ([68, 89, 45, 10, 20], [10, 20, 45, 68, 89])
        ]
        for test_case in basic_tests:
            linked_test = List()
            sorted_case = List()
            for i in test_case[0]:
                linked_test.insert(i)
            test_case[1].sort(reverse=True)
            for i in test_case[1]:
                sorted_case.insert(i)

            self.tests.append((linked_test, sorted_case))

        for i in range(0, 100):
            random_test = List()
            sorted_case = List()
            array = []
            for j in range(0, random.randint(0, 100)):
                randint = random.randint(0, 999)
                random_test.insert(randint)
                array.append(randint)

            array.sort(reverse=True)
            for k in array:
                sorted_case.insert(k)

            self.tests.append((random_test, sorted_case))

    def test_bubble_sort(self):
        for test in self.tests:
            linked_sorts.bubble_sort(test[0])
            self.assertTrue(test[0].is_identical(test[1]))

    def test_insertion_sort(self):
        for test in self.tests:
            linked_sorts.insertion_sort(test[0])
            self.assertTrue(test[0].is_identical(test[1]))

    def test_selection_sort(self):
        for test in self.tests:
            linked_sorts.selection_sort(test[0])
            self.assertTrue(test[0].is_identical(test[1]))

    def test_comb_sort(self):
        for test in self.tests:
            linked_sorts.comb_sort(test[0])
            self.assertTrue(test[0].is_identical(test[1]))

    def test_merge_sort(self):
        for test in self.tests:
            linked_sorts.merge_sort(test[0])
            self.assertTrue(test[0].is_identical(test[1]))

            #
            # def test_quick_sort(self):
            #     for test in self.tests:
            #         linked_sorts.quick_sort(test[0])
            #         self.assertEqual(test[0], test[1])


if __name__ == '__main__':
    unittest.main()
