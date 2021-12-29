class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue_rear(self, data):
        if self.rear is None:
            self.front = Node(data)
            self.rear = self.front
            return
        self.rear.next = Node(data)
        self.rear.next.prev = self.rear
        self.rear = self.rear.next

    def enqueue_front(self, data):
        if self.front is None:
            self.front = Node(data)
            self.rear = self.front
            return
        self.front.prev = Node(data)
        self.front.prev.next = self.front
        self.front = self.front.prev

    def dequeue_front(self):
        if self.front is None:
            return None
        else:
            temp = self.front.val
            self.front = self.front.next
            return temp

    def dequeue_rear(self):
        if self.rear is None:
            return None
        else:
            temp = self.rear.val
            self.rear = self.rear.prev
            return temp


if __name__ == '__main__':
    q = Deque()

    q.enqueue_front(1)
    q.enqueue_rear(2)
    q.enqueue_front(1000)
    q.enqueue_rear(40)
    q.enqueue_rear(50)
    q.enqueue_front(60)

    print(q.dequeue_front())
    print(q.dequeue_rear())
    print(q.dequeue_rear())
    print(q.dequeue_front())
    print(q.dequeue_rear())
    print(q.dequeue_front())
