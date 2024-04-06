# base case and recursive case
def factorial(x: int) -> int:
    if x < 1:
        return 1
    return x * factorial(x - 1)

print(factorial(5))