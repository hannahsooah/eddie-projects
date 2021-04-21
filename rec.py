def multiply(m, n):
    """
    >>> multiply(5, 3)
    15

    we need:
    - base case (something is zero, one) aka the ending condition
    - return
    - increment closer to the base case

    5 * 3 = 5 + 5 * 2 = 5 + 5 + 5 * 1
    ->
    multiply(5, 3) = 5 + multiply(5, 2) = 5 + 5 + multiply(5, 1)
    ->
    m = 5, n = 3
    multiply(m, n) = m + multiply(m, n - 1) = m + m + multiply(m, n - 2)
    ->
    """
    if m == 0:
        return 0
    if n == 0:
        return 0

    return m + multiply(m, n - 1)

def factorial(n):
    """
    >>> factorial(5)
    120
    >>> factorial(3)
    6
    >>> factorial(4)
    24

    we need:
    - base case (something is zero, one) aka the ending condition
    - increment closer to the base case

    factorial(5) = 5 * 4 * 3 * 2 * 1
    ->
    factorial(5) = 5 * factorial(4) = 5 * 4 * factorial(3) = 5 * 4 * 3 * factorial(2)
        = 5 * 4 * 3 * 2 * factorial(1) = 5 * 4 * 3 * 2 * 1
    ->
    factorial(n) = n * factorial(n - 1) = n * n-1 * factorial(n - 2) = n * n-1 * n-2 * factorial(n - 3)

    n = 5 -> => -> n = base case (ending condition, if statement)

    factorial(5) = 5 * factorial(4) = 5 * 4 * factorial(3) = 5 * 4 * 3 * factorial(2) = 5 * 4 * 3 * 2 * factorial(1)
        = 5 * 4 * 3 * 2 * 1 * factorial(0) = 5 * 4 * 3 * 2 * 1 * 0 = 0

    factorial(1) = 1 * factorial(0)
    factorial(0) = 0

    factorial(3) = 3 * factorial(2) = 3 * 2 * factorial(1) = 3 * 2 * 1

    """
    if n == 1:
        return 1
    return n * factorial(n - 1)

def fib(n):
    """
    Returns the n-th fibbonacci sequence

    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(7)
    13
    >>> fib(8)
    21
    >>> fib(9)
    34
    >>> fib(10)
    55

    it adds the previous 2 numbers together
    fib(n) = fib(n-1) + fib(n-2)
    fib(n-1) = fib(n-2) + fib(n-3)
    fib(n-2) = fib(n-3) + fib(n-4)

    fib(3) = fib(2) + fib(1) = 1 + 1 = 2
    fib(5) = fib(4) + fib(3) = (fib(3) + fib(2)) + (fib(2) + fib(1)) =
    fib(4) = fib(3) + fib(2)
    """
