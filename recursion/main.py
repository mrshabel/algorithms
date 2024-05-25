# base case and recursive case
def factorial(x: int) -> int:
    if x < 1:
        return 1
    return x * factorial(x - 1)

print(factorial(5))

def euclid_algorithm(x: int, y: int) -> int:
    """
    `Args`: x, y where x > y
    `Returns`: the gcd of x and y by using a recursive method
    """

    # base case
    if y == 0:
        return x
    
    # recursive case
    remainder = x % y
    x, y = y, remainder
    return euclid_algorithm(x, y)

print(euclid_algorithm(48, 18))

def fibonacci_sequence(n: int) -> int:
    """
    `Args`: n representing the nth fibonacci number
    """
    # base case
    if n <= 1:
        return n

    # recursive case
    return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)
