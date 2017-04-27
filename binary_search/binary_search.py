""" 
    Hyena yu
    lyuvictor@gmail.com
    Descriptions: implement binary search
"""


def binary_search(numbers, key, position):
    """ 
    numbers : a list of integer
    key : an integer element that being searching for
    position : an integer - starting position of the list 
    """
    i = position
    j = len(numbers) - 1
    while i <= j:
        m = int((i + j)/2)
        if numbers[m] < key:
            i = m + 1
        elif numbers[m] > key:
            j = m 
        else:
            return m
    return "not found"


if __name__ == '__main__':

    testList = [1, 3, 5, 6, 7, 8, 9, 10]
    print(binary_search(testList, 11, 0))
