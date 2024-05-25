class Stack:
    """
    An implemented of a stack data structure that uses an array under the hood by exposing only relevant stack methods to the user

    Methods:
        - push
        - pop
        - peek
        - is_empty
        - size
    """

    def __init__(self):
        self.stack = []

    # push
    def push(self, el: any):
        self.stack.append(el)

    # pop
    def pop(self) -> int:
        if self.is_empty:
            raise IndexError("Stack is Empty")
        return self.stack.pop()

    # peek
    def peek(self) -> None | int:
        if self.is_empty:
            return None
        return self.stack[-1]

    # isEmpty
    def is_empty(self) -> bool:
        return True if len(self.stack) else False

    # size
    def size(self) -> int:
        return len(self.stack)
