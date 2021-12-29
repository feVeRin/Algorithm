class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        cur = self.top
        self.top = Node(data)
        self.top.next = cur

    def pop(self):
        pop = self.top.val
        self.top = self.top.next
        return pop

    def peak(self):
        return self.top.val


if __name__ == '__main__':
    s = Stack()

    s.push(1)
    s.push(3)
    s.push(5)
    s.push(2)

    for _ in range(4):
        print(s.pop())
