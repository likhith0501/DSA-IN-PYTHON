##stack Implementation (Using List)


##Concept: Stack follows LIFO (Last In First Out).

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(item, "pushed")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()

print("Popped:", s.pop())
s.display()