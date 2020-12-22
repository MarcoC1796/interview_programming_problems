# Problem: design a stack that includes a max operation, in addition to push and pop. The max method
#          should return the maximum value stored in the stack

# EPI Judge: stack_with_max.py
class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def push(self, element):
        max_top = element
        if not self.empty():
            max_top = max(max_top, self.stack[-1][1])
        self.stack.append((element, max_top))

    def pop(self):
        return self.stack.pop()[0]

    def peek(self):
        if not self.empty():
            return self.stack[-1][0]

    def max(self):
        if not self.empty():
            return self.stack[-1][1]
        else:
            return None