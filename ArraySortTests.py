__author__ = 'Q'

import unittest
import random
import array_sorts


class SortTests(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ([], []),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([3, 2, 1], [1, 2, 3]),
            ([5, 9, 1, 6], [1, 5, 6, 9]),
            ([68, 89, 45, 10, 20], [10, 20, 45, 68, 89])]

        for i in range(0, 100):
            random_test = []
            for j in range(0, random.randint(0, 100)):
                random_test.append(random.randint(0, 999))
            unsorted = random_test
            random_test.sort()
            self.tests.append((unsorted,random_test))

    def test_bubble_sort(self):
        for test in self.tests:
            array_sorts.bubble_sort(test[0])
            self.assertEqual(test[0], test[1])

    def test_insertion_sort(self):
        for test in self.tests:
            array_sorts.insertion_sort(test[0])
            self.assertEqual(test[0], test[1])

    def test_selection_sort(self):
        for test in self.tests:
            array_sorts.selection_sort(test[0])
            self.assertEqual(test[0], test[1])

    def test_comb_sort(self):
        for test in self.tests:
            array_sorts.comb_sort(test[0])
            self.assertEqual(test[0], test[1])

    def test_merge_sort(self):
        for test in self.tests:
            array_sorts.merge_sort(test[0])
            self.assertEqual(test[0], test[1])

    def test_quick_sort(self):
        for test in self.tests:
            array_sorts.quick_sort(test[0])
            self.assertEqual(test[0], test[1])


if __name__ == '__main__':
    unittest.main()
