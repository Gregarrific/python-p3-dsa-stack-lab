class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def push(self, item):
        if len(self.items) < self.limit:
            return self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()

    def peek(self):
        return self.items
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) == self.limit:
            return True
        else:
            return False

    def search(self, target):
        stack = self.items
        try:
            position = stack.index(target)
            return len(self.items) - position - 1
        except ValueError:
            return -1
