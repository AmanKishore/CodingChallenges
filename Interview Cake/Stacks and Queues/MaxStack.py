'''
Max Stack
    Implement a new class MaxStack with a method get_max() that returns the largest element in the stack.
'''

class MaxStack:
    
    def __init__(self):
        self.stack = []
        self.max = []

    def push(self, item):
        self.stack.append(item)
        if not self.max or item >= self.max[-1]: # If the item is greater than or equal to the last item in max
            self.max.append(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.max[-1]:   # If it equals the top item in max then pop
            self.max.pop()
        return item

    def get_max(self):
        return self.max[-1]