class MyStackInt:
    def __init__(self):
        self.items = []
        self.__max_stack = []

    def push(self, item: int):

        if self.is_empty():
            self.__max_stack.append(item)
        elif item >= self.__max_stack[-1]:
            self.__max_stack.append(item)
        self.items.append(item)

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from empty stack')
        if self.items[-1] == self.__max_stack[-1]:
            self.__max_stack.pop()
        return self.items.pop()

    def max(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.__max_stack[-1]
