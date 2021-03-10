def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    1. pick a positive integer n as the start
    2. if n is even, divide it by 2
    3. if n is odd, multiply if by 3 and add 1
    4. continue this process until n is 1

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"

    """
    1. find the remainder and see if it's even or odd
    2. if, else statement
    """
    #while (a != 0):
    #    print("a is not zero")
    #    a = a - 1
    #print("a is zero")
    print(n)
    length = 1
    while (n != 1):
        length = length + 1
        if n % 2 == 0:
            n = n / 2
            print(n)
        else:
            n = n * 3 + 1
            print(n)
    if n == 1:
        print("wow!!!")
        return length
