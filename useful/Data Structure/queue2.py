class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.rear is None:
            self.front = Node(data)
            self.rear = self.front
            return
        self.rear.next = Node(data)
        self.rear.next.prev = self.rear
        self.rear = self.rear.next

    def dequeue(self):
        if self.front is None:
            return None
        else:
            temp = self.front.val
            self.front = self.front.next
            return temp

    def peek(self):
        if self.front is None:
            return None
        else:
            return self.front.val


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(1000)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)

    print(q.peek())

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    print(q.peek())
