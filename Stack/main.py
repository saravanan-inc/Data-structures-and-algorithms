"""
Stack Data Structure
FILO
Push, Pop, isEmpty, isFull, Peek
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def peek(self):
        print(self.stack)


s = Stack()

# Pop
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

s.peek()

s.pop()
s.pop()
s.pop()

s.peek()
