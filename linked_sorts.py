__author__ = 'Q'


def linked_swap(a, index_a, index_b):
    temp = a[index_b]
    a.replace(index_b, a[index_a])
    a.replace(index_a, temp)


def insertion_sort(a):
    """
    -------------------------------------------------------
    Sorts a linked list using the Insertion Sort algorithm.
    Use: insertion_sort( a )
    -------------------------------------------------------
    Preconditions:
      a - a linked list of comparable elements (List)
    Postconditions:
      Contents of a are sorted.
    -------------------------------------------------------
    """

    unsorted_start_index = 1
    while unsorted_start_index < len(a):

        if a[unsorted_start_index] < a[unsorted_start_index - 1]:
            swapping_index = unsorted_start_index
            while swapping_index > 0 and a[swapping_index] < a[swapping_index - 1]:
                linked_swap(a, swapping_index - 1, swapping_index)
                swapping_index -= 1
        unsorted_start_index += 1


def selection_sort(a):
    """
    -------------------------------------------------------
    Sorts a linked list using the Selection Sort algorithm.
    Use: selection_sort( a )
    -------------------------------------------------------
    Preconditions:
      a - a linked list of comparable elements (List)
    Postconditions:
      Contents of a are sorted.
    -------------------------------------------------------
    """
    sorted_index = 0
    while sorted_index < len(a) - 1:
        unsorted_index = sorted_index + 1
        min_value = a[sorted_index]
        min_index = sorted_index
        while unsorted_index < len(a):
            if min_value > a[unsorted_index]:
                min_value = a[unsorted_index]
                min_index = unsorted_index
            unsorted_index += 1
        linked_swap(a, min_index, sorted_index)
        sorted_index += 1


def bubble_sort(a):
    """
    -------------------------------------------------------
    Sorts a linked list using the Bubble Sort algorithm.
    Use: bubble_sort( a )
    -------------------------------------------------------
    Preconditions:
      a - a linked list of comparable elements (List)
    Postconditions:
      Contents of a are sorted.
    -------------------------------------------------------
    """
    swapped = True
    i = 0
    while i < len(a) and swapped:
        swapped = False
        j = 0
        while j < len(a) - 1:
            if a[j] > a[j + 1]:
                linked_swap(a, j, j + 1)
                swapped = True
            j += 1
        i += 1


def comb_sort(a):
    """
    -------------------------------------------------------
    Sorts a linked list using the Comb Sort algorithm.
    Use: comb_sort( a )
    -------------------------------------------------------
    Preconditions:
      a - a linked list of comparable elements (List)
    Postconditions:
      Contents of a are sorted.
    -------------------------------------------------------
    """

    swapped = True
    gap = len(a)
    shrink = 1.3

    while gap > 1 or swapped:
        gap = int(gap / shrink)
        gap = max(gap, 1)
        swapped = False
        i = 0
        while i + gap < len(a):
            if a[i] > a[i + gap]:
                linked_swap(a, i, i + gap)
                swapped = True
            i += 1


def merge_sort(a):
    """
    -------------------------------------------------------
    Sorts a linked list using the Merge Sort algorithm.
    Use: merge_sort( a )
    -------------------------------------------------------
    Preconditions:
      a - a linked list of comparable elements (List)
    Postconditions:
      Contents of a are sorted.
    -------------------------------------------------------
    """
    _merge_sort_aux(a, 0, len(a) - 1)

    return


def _merge_sort_aux(a, low, high):
    if low < high:
        mid = (high - low) // 2 + low
        _merge_sort_aux(a, low, mid)
        _merge_sort_aux(a, mid + 1, high)
        _merge(a, low, mid, high)


def _merge(a, low, mid, high):
    temp = []
    i = low
    j = mid + 1

    while i <= mid and j <= high:
        if a[i] <= a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1
    [temp.append(a[x]) for x in range(i, mid + 1)]
    [temp.append(a[y]) for y in range(j, high + 1)]
    for k in range(len(temp)):
        a.replace(low + k, temp[k])


