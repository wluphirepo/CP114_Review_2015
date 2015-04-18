import unittest

__author__ = 'Q'


def is_palindrome(word):
    front = 0
    end = -1
    palindrome = True
    mid = len(word)//2

    while front < mid and palindrome:
        if word[front] != word[end]:
            palindrome = False
        front += 1
        end -= 1
    return palindrome


if __name__ == "__main__":
    x = input("Input: ")
    print(is_palindrome(x))




class PalindromeTests(unittest.TestCase):
    def test_odd_length(self):
        word = 'kayak'
        expected = True
        actual = is_palindrome(word)
        self.assertEqual(expected, actual)

    def test_even_length(self):
        word = 'anna'
        expected = True
        actual = is_palindrome(word)
        self.assertEqual(expected, actual)

    def test_single_character(self):
        word = 'a'
        expected = True
        actual = is_palindrome(word)
        self.assertEqual(expected, actual)

    def test_gibberish(self):
        word = 'asdfaser234adfasdf'
        expected = False
        actual = is_palindrome(word)
        self.assertEqual(expected, actual)