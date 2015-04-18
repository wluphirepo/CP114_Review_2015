"""
-------------------------------------------------------
list_linked.py
-------------------------------------------------------
Author:  David Brown
ID:
Email:   dbrown@wlu.ca
Version: 2015-04-01
-------------------------------------------------------
Linked version of the List ADT.
-------------------------------------------------------
"""
import copy


class _ListNode:
    def __init__(self, value, next_node):
        """
        -------------------------------------------------------
        Initializes a list node.
        Use: node = _ListNode(value, next_node)
        -------------------------------------------------------
        Preconditions:
            value - data value for node (?)
            next_node - another list node (_ListNode)
        Postconditions:
            Initializes a List node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._value = copy.deepcopy(value)
        self._next = next_node
        return


# -------------------------------------------------------
class List:
    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: l = List()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty list.
        -------------------------------------------------------
        """
        self._front = None
        self._count = 0
        return

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element. (?)
        Postconditions:
            returns:
            True if the list contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        _, current, _ = self._linear_search(key)

        if current is None:
            result = False
        else:
            result = True
        return result

    def __getitem__(self, n):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[n]
        -------------------------------------------------------
        Preconditions:
            n - index of the element to access. (int)
        Postconditions:
            returns:
            value - the nth element of list if it exists, None if n
            is outside the array boundaries of the list. (?)
        -------------------------------------------------------
        """
        if n >= 0 and n < self._count:
            i = 0
            current = self._front

            while i < n:
                current = current._next
                i += 1
            value = copy.deepcopy(current._value)
        else:
            value = None
        return value

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len( l )
        -------------------------------------------------------
        Postconditions:
            returns:
            the number of values in the list. (int)
        -------------------------------------------------------
        """
        return self._count

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first copy of key in the list.
        Private helper operations - used only by other ADT operations.
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Preconditions:
            key - a data element. (?)
        Postconditions:
            returns:
            previous - the node previous to the node containing value,
            None if there is no previous node. (_ListNode)
            current - the node containing value, None if there is no
            node containing value (_ListNode)
            index - the index of key in the list, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        # Find the proper _value in the list.
        current = self._front
        previous = None
        index = 0

        while current is not None and key != current._value:
            previous = current
            current = current._next
            index += 1

        if current is None:
            index = -1

        return previous, current, index

    def apply(self, func):
        """
        -------------------------------------------------------
        Applies an external function to every value in list.
        -------------------------------------------------------
        Preconditions:
            func - a function that takes a single value as a parameter
            and returns a value (function)
        Postconditions:
            All elements of the list have func applied to them.
        -------------------------------------------------------
        """

        # your code here

        return

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list.
        Use: l.clean()
        -------------------------------------------------------
        Postconditions:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """

        # your code here

        return

    # def copy(self):
    #     """
    #     -------------------------------------------------------
    #     Duplicates the current list to a new list in the same order.
    #     Use: new_list = l.copy()
    #     -------------------------------------------------------
    #     Postconditions:
    #         returns:
    #         new_list - a copy of self (List)
    #     -------------------------------------------------------
    #     """
    #     new_list = List()
    #
    #
    #     # your code here
    #
    #     return new_list

    # def copy_r(self, rhs):
    #     """
    #     -----------------------------------------------------------
    #     Duplicates the current list to a new list in the same order.
    #     (recursive)
    #     Use: new_list = l.copy()
    #     -----------------------------------------------------------
    #     Postconditions:
    #         returns:
    #         new_list - contains copies of the values of self
    #         in the same order (List)
    #     -----------------------------------------------------------
    #     """
    #     new_list = List()
    #     new_list._front = self._copy_r_aux(self._front)
    #     new_list._count = self._count
    #     return
    #
    # def _copy_r_aux(self, current):
    #     """
    #     -----------------------------------------------------------
    #     Auxiliary function for copy_r. Private helper function
    #     Use: new_node = self._copy_r_aux(current)
    #     -----------------------------------------------------------
    #     Preconditions:
    #         current - current list node to be copied (_ListNode)
    #     Postconditions:
    #         returns:
    #         new_node - new node of new list (_ListNode)
    #     -----------------------------------------------------------
    #     """
    #
    #     # your code here
    #
    #     return new_node

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: l.count(key)
        -------------------------------------------------------
        Postconditions:
            returns:
            number - the number of times key appears in list. (int)
        -------------------------------------------------------
        """
        number = 0
        current = self._front

        while current is not None:
            if key == current._value:
                number += 1
            current = current._next
        return number

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the the value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Preconditions:
            key - a data element. (?)
        Postconditions:
            returns:
            value - a copy of the full value matching key, otherwise None. (?)
        -------------------------------------------------------
        """
        _, current, _ = self._linear_search(key)

        if current is None:
            value = None
        else:
            value = copy.deepcopy(current._value)
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Preconditions:
            key - a data element (?)
        Postconditions:
            returns:
            i - the index of the location of key in the list, -1 if
            key is not in the list. (int)
        -------------------------------------------------------
        """
        _, _, n = self._linear_search(key)
        return n

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the list.
        Use: l.insert( value )
        -------------------------------------------------------
        Preconditions:
            value - a data element. (?)
        Postconditions:
            value is added to the front of the list.
        -------------------------------------------------------
        """
        node = _ListNode(value, self._front)
        self._front = node
        self._count += 1
        return

    # def intersection(self, second):
    #     """
    #     -------------------------------------------------------
    #     Returns a list that contains only values that appear in both
    #     the current List and second.
    #     Use: l2 = 11.intersection(second)
    #     -------------------------------------------------------
    #     Preconditions:
    #         second - another List (List)
    #     Postconditions:
    #         returns:
    #         new_list - A List that contains only the values found in both
    #         the current List and second. Values do not repeat. (List)
    #     -------------------------------------------------------
    #     """
    #
    #     # your code here
    #
    #     return new_list

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = l.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns:
            True if the list is empty, False otherwise. (boolean)
        -------------------------------------------------------
        """
        return self._front is None

    def is_identical(self, rhs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical, i.e. same values appear
        in the same locations in both lists.
        Use: b = l.is_identical( rhs )
        -------------------------------------------------------
        Preconditions:
            rhs - another list (List)
        Postconditions:
            returns:
            identical - True if this list contains the same values as rhs
            in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        if self._count != rhs._count:
            identical = False
        else:
            current_self = self._front
            current_rhs = rhs._front

            while current_self is not None and current_self._value == current_rhs._value:
                current_self = current_self._next
                current_rhs = current_rhs._next

            identical = current_self is None
        return identical

    def is_identical_r(self, rhs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical, i.e. same values appear
        in the same locations in both lists. (recursive)
        Use: b = l.is_identical( rhs )
        -------------------------------------------------------
        Preconditions:
            rhs - another list (List)
        Postconditions:
            returns:
            identical - True if this list contains the same values as rhs
            in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        if self._count != rhs._count:
            identical = False
        else:
            identical = self._is_identical_r_aux(self._front, rhs._front)
        return identical

    def _is_identical_r_aux(self, current_self, current_rhs):
        """
        -------------------------------------------------------
        An auxiliary function for list_identical_r
        Use: identical = self.._is_identical_r_aux(left_node, right_node)
        -------------------------------------------------------
        Preconditions:
            current_self - a List node (_ListNode)
            current_rhs - a List node (_ListNode)
        Postconditions:
            returns:
            identical - True if list starting with current_self is identical
              to list starting with current_rhs, otherwise False. (boolean)
        -------------------------------------------------------
        """
        if current_self is None and current_rhs is None:
            identical = True
        elif current_self._value != current_rhs._value:
            identical = False
        else:
            identical = self._is_identical_r_aux(current_self._next,
                                                 current_rhs._next)
        return identical

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = l.max()
        -------------------------------------------------------
        Postconditions:
            returns:
            max_value - a copy of the first maximum value in the list,
            None if the list is empty. (?)
        -------------------------------------------------------
        """
        if self._front is None:
            max_value = None
        else:
            max_node = self._front
            current = self._front._next

            while current is not None:
                if max_node._value < current._value:
                    max_node = current
                current = current._next
            max_value = copy.deepcopy(max_node._value)
        return max_value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = l.min()
        -------------------------------------------------------
        Postconditions:
            returns:
            min_value - a copy of the first minimum value in the list,
            None if the list is empty. (?)
        -------------------------------------------------------
        """
        if self._front is None:
            min_value = None
        else:
            min_node = self._front
            current = self._front._next

            while current is not None:
                if min_node._value > current._value:
                    min_node = current
                current = current._next
            min_value = copy.deepcopy(min_node._value)
        return min_value

    def print_i(self):
        """
        -------------------------------------------------------
        Prints the contents of list.
        Use: l.print_i()
        -------------------------------------------------------
        Postconditions:
            Prints each value in list.
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            print(current._value)
            current = current._next
        return

    def print_r(self):
        """
        -------------------------------------------------------
        Prints the contents of list from rear to front.
        Use: l.print_r()
        -------------------------------------------------------
        Postconditions:
          Prints each value in list.
        -------------------------------------------------------
        """
        self._print_r_aux(self._front)
        return

    def _print_r_aux(self, current):
        """
        -------------------------------------------------------
        Prints the contents of the current node.
        -------------------------------------------------------
        Postconditions:
          Prints the value in the current node.
        -------------------------------------------------------
        """
        if current is not None:
            self._print_r_aux(current._next)
            print(current._value)
        return

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list that matches key.
        Use: value = l.remove( key )
        -------------------------------------------------------
        Preconditions:
            key - a data element (?)
        Postconditions:
            returns:
            value - the full value matching key, otherwise
            returns None. value is removed from the list. (?)
        -------------------------------------------------------
        """
        # Find the proper _value in the list.
        previous, current, _ = self._linear_search(key)

        if current is None:
            # key not found in list
            value = None
        elif previous is None:
            # key is in first node in list.
            value = self._front._value
            self._front = self._front._next
            self._count -= 1
        else:
            # key is in some other node in list
            value = current._value
            self._count -= 1
            previous._next = current._next
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list.
        Use: value = l.remove_front()
        -------------------------------------------------------
        Postconditions:
            returns:
            value - the first value in the list, None if the list is empty (?)
        -------------------------------------------------------
        """
        if self._front is None:
            value = None
        else:
            value = self._front._value
            self._front = self._front._next
            self._count -= 1
        return value

    def remove_many(self, key):
        """
        ---------------------------------------------------------
        Finds, removes, and returns the value in list that matches key.
        Use: l.remove_many( key )
        -------------------------------------------------------
        Preconditions:
            key - a data element (?)
        Postconditions:
            Removes all values matching key.
        ---------------------------------------------------------
        """
        # Find the proper _value in the list.
        current = self._front
        previous = None

        while current is not None:

            if current._value == key:
                # Remove the current node.
                if previous == None:
                    self._front = self._front._next
                    current = self._front
                else:
                    previous._next = current._next
                    current = current._next
                self._count -= 1
            else:
                previous = current
                current = current._next
        return

    def replace(self, n, value):
        """
        -------------------------------------------------------
        Preconditions:
            n - index of the element to access (int)
            value - a data value (?)
        Postconditions:
            returns:
            old_value - the old value that is being replaced if n
            is valid, None otherwise. (?)
        -------------------------------------------------------
        """
        if n >= 0 and n < self._count:
            i = 0
            current = self._front

            while i < n:
                current = current._next
                i += 1

            old_value = current._value
            current._value = copy.deepcopy(value)
        else:
            old_value = None
        return old_value

    def replace_key(self, key, new_value):
        """
        -------------------------------------------------------
        Replace every occurrence of key in list with new_value.
        Use: l.replace( key, new_value )
        -------------------------------------------------------
        Preconditions:
            key - a key value that may be in l (?)
            new_value - the replacement for value with key (?)
        Postconditions:
            All copies of key are replace with new_value.
        -------------------------------------------------------
        """

        # your code here

        return

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        Use: l.reverse()
        -------------------------------------------------------
        Postconditions:
            The contents of list are reversed in order with respect
            to their order before the operation was called.
        -------------------------------------------------------
        """

        # your code here

        return

    # def reverse_r(self):
    #     """
    #     -------------------------------------------------------
    #     Reverses the order of the elements in list.
    #     (recursive)
    #     Use: l.reverse_r()
    #     -------------------------------------------------------
    #     Postconditions:
    #         The contents of list are reversed in order with respect
    #         to their order before the operation was called.
    #     -------------------------------------------------------
    #     """
    #     self._front = self._reverse_r_aux(self._front)
    #     return

    # def _reverse_r_aux(self, node):
    #     """
    #     -------------------------------------------------------
    #     Reverses the order of the elements in list.
    #     (recursive)
    #     Use: node = self._reverse_r_aux(node)
    #     -------------------------------------------------------
    #     Postconditions:
	 #    returns:
	 #    current - the replacement node for the curent node (_ListNode)
    #         The contents of node are reversed in order with respect
    #         to their order before the operation was called.
    #     -------------------------------------------------------
    #     """
    #
    #     # your code here
    #
    #     return current

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits list into two parts with values alternating between
        the two lists. Order need not be preserved.
        Use: new_list = l.split_alt()
        -------------------------------------------------------
        Postconditions:
            returns:
            new_list - a new List with <= 50% of the original List. Current
            List contains >= 50% of the original List.
        -------------------------------------------------------
        """
        new_list = List()

        # your code here

        return new_list

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Splits list into two parts with values alternating between
        the two lists. (recursive)
        Use: new_list = l.split_alt_r()
        -------------------------------------------------------
        Postconditions:
            returns:
            new_list - a new List with <= 50% of the original List. Current
            List contains >= 50% of the original List.
        -------------------------------------------------------
        """
        new_list = List()
        new_list._front = self._split_alt_r_aux(self._front)
        new_list._count = self._count // 2
        self._count = self._count - new_list._count
        return new_list

    # def _split_alt_r_aux(self, current):
    #     """
    #     -------------------------------------------------------
    #     Splits current into two parts.
    #     -------------------------------------------------------
    #     Preconditions:
    #         current - a List node (_ListNode)
    #     Postconditions:
    #         returns:
    #         node - the node following current (_ListNode)
    #         current._next is updated to point to the node following node
    #     -------------------------------------------------------
    #     """
    #
    #     # your code here
    #
    #     return node

    def split_counter(self):
        """
        -------------------------------------------------------
        Splits list into two parts. Current List contains the first half,
        the new_list List the new_list half. Uses counter algorithm.
        -------------------------------------------------------
        Postconditions:
            returns:
            new_list - a new List with <= 50% of the original List. Current
            List contains >= 50% of the original List.
        -------------------------------------------------------
        """
        new_list = List()

        # your code here

        return new_list

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. Current List contains the first half,
        the new_list List the new_list half. Uses Tortoise / Hare algorithm.
        -------------------------------------------------------
        Postconditions:
            returns:
            new_list - a new List with <= 50% of the original List. Current
            List contains >= 50% of the original List.
        -------------------------------------------------------
        """
        new_list = List()

        # your code here

        return new_list

    def union(self, second):
        """
        -------------------------------------------------------
        Returns a list that contains all values in both
        the current List and second.
        Use: nl = l.union(second)
        -------------------------------------------------------
        Preconditions:
            second - another list (List)
        Postconditions:
            returns:
            new_list - contains all values found in both the current
            List and second. Values do not repeat. (List)
        -------------------------------------------------------
        """
        new_list = List()

        # your code here

        return new_list


