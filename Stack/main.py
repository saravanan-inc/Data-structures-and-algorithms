'''
    1. Start
    2. Initialize 
        top = -1
    3. Push
        Increment Top
        array[top] = value
    4. Pop
        temp = array[top]
        top -= 1
        return temp
'''


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()


s = Stack()
s.push(1)
print(s.stack)

s.pop()
print(s.stack)
