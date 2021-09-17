'''
Stack Data Stucture
push(n)
pop()
is_empty()
peek()
'''


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if (len(self.items) is not 0):
            return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items is []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")
print (stack.get_stack())
print(stack.pop())
print (stack.get_stack())
print (stack.peek())
print (stack.is_empty())
