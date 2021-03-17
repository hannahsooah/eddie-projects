"Q1"

def falling(n, k):
    """
    falling factorial takes two arguments n and k, and returns the product of
    k consecutive numbers starting from n and working downwards

    >>> falling(6, 3) # 6 * 5 * 4
    120
    >>> falling(4, 3) # 4 * 3 * 2
    24
    >>> falling(4, 1) # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"

    """
    6 * 5 * 4

    n * (n-1) * (n-2) until we get to k arguments

    we need to keep track of the length (number of arguments)

     variable "product"

    while loop: ends when length = k ==> while (length != k)
    n = 6, k = 3
    product = 6                                 length = 1
    product = 6 * (5)                           length = 2
    product = 6 * 5 * 4 = 30 * (4) = 120        length = 3

    product = 4 = 4 * 1 = (n-length) * product  length = 1
    product = 4 * 3 = product * (n-length)      length = 2
    product = 4 * 3 * 2 = product * (n-length)  length = 3


    n = 4
    k = 3
    product = 24
    length = 2
    """
    product = 1
    length = 0

    while (length != k):
        # whatever your loop is
        product = product * (n-length)
        length = length + 1
    # whatever is outside your loop
    return product

    """length == 1

    while(k != 0):
        k = k - 1
        length = length + 1

    while(n != 0):
        (n * n) * length - 1
    """


"Q2"

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    >>>  sum_digits(435)
    12
    """
    "*** YOUR CODE HERE ***"

    """
    BRAINSTORM HERE

    tips:
    a % 10 returns last digit of a
        234987 % 10 returns 7
        32985 % 10 returns 5
    a // 10 returns a without the last digit
        234987 // 10 returns 23498
        32985 // 10 returns 3298


    a % b to make a last digit + sentence
     use a // 10 to make a new last digit,
     use a%b to make a last digit + sentence

    sum_digits(4224)

    answer = 12
    y = 0
    """

    answer = 0

    while (y > 0):
        answer = answer + y % 10
        y = y // 10

    return answer



    """

"Q3"
def cancel_culture(n, k):
    while (k != 0):
        number = k - 1
        n * number
        return (number)

    doctests:

    >>> cancel_culture(4, 3)





    >>> cancel_culture(2, 1)

    >>> cancel_culture(6, 2)

    """
