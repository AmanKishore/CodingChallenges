'''
Queue Two Stacks
Implement a Queue with two Stacks
'''

class QueueTwoStacks:
    
    def __init__(self):
        self.ins  = []
        self.outs = []

    def enqueue(self, item):
        self.ins.append(item)

    def dequeue(self):
        if len(self.outs) == 0:

            while len(self.ins) > 0:  # Move items from ins to outs, reversing order
                self.outs.append(self.ins.pop())

            if len(self.outs) == 0:   # If outs is still empty, raise an error
                raise IndexError("Can't dequeue from empty queue!")

        return self.outs.pop()