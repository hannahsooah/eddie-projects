def first_last(list):
    """
    Prints the first and last elements in the given list. If the list only has
    one elements, only display that element once. If the list has less than one
    element, then display an error message of "Please enter a non-empty list."

    >>> first_last(["Red", "Green", "White", "Black"])
    Red Black
    >>> first_last([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    0 9
    >>> first_last([])
    Please enter a non-empty list.
    >>> first_last(["Hello World"])
    Hello World
    """

    """
    0, 1, 2, 3, 4, ...
    list = ["Red", "Green", "White", "Black"]
    list[0] will return "Red"
    list[1] will return "Green"
    list[2] will return "White"
    list[3] will return "Black"
    len(list) will return the length of the list
    list[-1] will return the last element in the list
    list[-2] will return the second to last element in the list
    """

    if len(list) > 0:
        if len(list) == 1:
            print(list[0])
        else:
            print(list[0],list[-1])
    else:
        print("Please enter a non-empty list.")

def circle(r):
    """
    Returns the area of a circle given the radius.
    r: int for radius

    >>> circle(1)
    3.14
    >>> circle(2)
    12.56
    >>> circle(11.345)
    404.1463385
    """

    """
    the area of a circle is equal to pi * r^2
    you can assume pi = 3.14
    """
    return r * r * 3.14

def contains(list, x):
    """
    Given a list and element, return whether the element
    is contained in the list.
    >>> contains([1, 5, 3, 8], 3)
    True
    >>> contains([1, 5, 3, 8], 7)
    False
    >>> contains(["Hello", "World"], "Hello")
    True
    >>> contains(["Hello", "World"], "bye")
    False
    >>> contains(["Hello", "World"], 3)
    False
    """

    """
    list_results = [ ______ for y in list ]
    >>> contains([1, 5, 3, 8], 3)
    list_results = [ elem == 1 for elem in list ]
    >>> print(list_results)
    [True, False, False, False]

    any(list) returns True if any element in the list is True. returns False if
    all elements in the list are False.
    """

    if any([elem == x for elem in list]):
        return True
    else:
        return False

def not_in(l1, l2):
    """
    Return a list containing all the elements from list 1 (l1) that are not in list 2 (l2).
    Print the message "There are no elements from list 1 that are not in list 2." if the message
    is true and return nothing.

    >>> not_in([1, 2, 3],[4, 5, 6])
    [1, 2, 3]
    >>> not_in(["Hello", "World"],["Hello"])
    ["World"]
    >>> not_in([1],[1, 2])
    There are no elements from list 1 that are not in list 2.
    """

    """
    HINT:

    [___ for elem in list]

    for elem in list:
        _______

    list = ["hello", "world"]
    sum = ""
    for elem in list:
        sum = sum + elem

    1st time: elem = 1
    - sum = sum + elem ==> sum = 0 + 1 ==> sum = 1
    2nd time: elem = 2
    - sum = sum + elem ==> sum = 1 + 2 ==> sum = 3
    3rd time: elem = 3
    - sum = sum + elem ==> sum = 3 + 3 ==> sum = 6

    1st time: elem = "hello"
    - sum = sum + elem ==> sum = "" + "hello" ==> sum = "hello"
    2nd time: elem = "world"
    - sum = sum + elem ==> sum = "hello" + "world" ==> sum = "helloworld"

    list.append(something) will add the something to the end of the list.
    """


    """
    what is list supposed to contain?
    - the numbers that are in l1 and not in l2

    """
    list = []
    for elem in l1:
        if not contains(l2, elem):
            list.append(elem)
    return list

def gcd(a, b):
    """
    Return the greatest common divisor of two positive integers.

    >>> gcd(5, 10)
    5
    >>> gcd(12, 18)
    6
    >>> gcd(41, 5)
    1
    >>> gcd(51, 17)
    17
    """

    """
    HINT:
    check each number from 1 to the smaller positive integer to see if it divides both
    integers evenly. if the mod (%) is zero, then the number divides evenly and is a
    divisor (by definition).
    i.e. if x % y = 0, then y is a divisor of x

    gcd(5, 10):
        10 % 5 == 0
        5 is a divisor of both 5 and 10
        return 5
    gcd(12, 18):
        18 % 12 == 6
        18 % 11 == 5 and 12 % 11 == 1
        18 % 10 == 8 and 12 % 10 == 2
        18 % 9 == 0 and 12 % 9 == 3
        18 % 8 == 2 and 12 % 8 == 4
        18 % 7 == 4 and 12 % 7 == 5
        18 % 6 == 0 and 12 % 6 == 0
        6 is a divisor of both 12 and 18
        return 6
    greatest common divisor
    gcd(41, 5):
        x = min(41, 5) = 5
        while (a % x != 0) and (b % x != 0):
        while (41 % 5 != 0) and (5 % 5 != 0):
        while False and True:
            x = x - 1 = 4
    until a % x == 0 and b % x == 0
    if a % x != 0
    or if b % x != 0

    """
    x = min(a, b)
    while not (a % x == 0 and b % x == 0):
        x = x - 1
    return x

def lcm(a, b):
    """
    Return the lowest common multiple of two positive integers a and b.

    >>> lcm(35, 5)
    35
    >>> lcm(12, 18)
    36
    >>> lcm(2, 4)
    4
    >>> lcm(2, 3)
    6
    >>> lcm(9, 24)
    72
    """

    """
    HINT:
    x = max(a, b)
    lcm(12, 18)
    x = 18
    18 % 12 == 6
    x * 2 = 36
    36 % 12 == 0
    return 36

    lcm(9, 24):
    x = 24
    24 % 9 = 6
    x = 48
    48 % 9 = 3
    72 % 9 = 0
    return 72

    """

    x = max(a,b)
    y = min(a,b)
    z = x
    while x % y != 0:
        x = x + z
    return x

def div2(x):
    return x / 2
def pow(x):
    return x * x
def mul9(x):
    return x * 9
def char(s):
    return s[0]

def apply(f, list):
    """
    Return a list with the function f applied to every element of list.

    >>> apply(circle, [1, 2, 3])
    [3.14, 12.56, 28.26]
    >>> apply(sqrt, [4, 9, 16])
    [2, 3, 4]
    >>> apply(div2, [9, 4, 7])
    [4.5, 2, 3.5]
    >>> apply(pow, [9, 12, 4])
    [81, 144, 16]
    >>> apply(char, ["hello", "world", "this", "is", "eddie"])
    ["h", "w", "t", "i", "e"]
    """

    """
    HINT:

    [ ____ for elem in list]
    where ___ can be anything pertaining to the element

    apply(circle, [1, 2, 3])
    [1, 2, 3]
    [circle(1), circle(2), circle(3)]
    return [3.14, 12.56, 28.26]

    """

    list2 = [f(elem) for elem in list]
    return list2
