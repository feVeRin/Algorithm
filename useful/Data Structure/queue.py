class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if not self.front:
            return True
        return False

    def enqueue(self, data):
        new = Node(data)

        if self.is_empty():
            self.front = new
            self.rear = new
            return

        self.rear.next = new
        self.rear = new

    def dequeue(self):
        if self.is_empty():
            return None

        deq = self.front.val
        self.front = self.front.next
        return deq

    def peek(self):
        if self.is_empty():
            return None
        return self.front.val


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(100)
    q.enqueue(40)
    q.enqueue(3)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.peek())
    print(q.dequeue())
    print(q.dequeue())
