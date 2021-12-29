class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0
        self.size = 0

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
            self.size += 1
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(val)
            self.size += 1

    def print(self):
        cur = self.head
        while cur:
            if cur.next is not None:
                print(cur.val, ' -> ', end='')
            else:
                print(cur.val)
            cur = cur.next

    def search(self, idx):
        cur = self.head
        i = 0
        while i < idx:
            cur = cur.next
            i += 1
        return cur

    def insert(self, idx, val):
        if idx == 0:
            new_node = Node(val)

            temp = self.head
            self.head = new_node
            self.head.next = temp

            self.size += 1
        elif idx == self.size:
            cur = self.search(idx-1)

            new_node = Node(val)
            cur.next = new_node
            self.size += 1
        else:
            cur = self.search(idx)

            new_node = Node(val)
            temp = cur.next
            cur.next = new_node
            new_node.next = temp

            self.size += 1

    def delete(self, idx):
        if idx == 0:
            temp = self.head
            self.head = temp.next
            self.size -= 1
            del temp
        else:
            prev_node = self.search(idx-1)
            temp = prev_node.next
            prev_node.next = prev_node.next.next
            self.size -= 1
            del temp

    def reverse(self):
        cur, prev = self.head, None

        while cur:
            nxt, cur.next = cur.next, prev
            prev, cur = cur, nxt

        self.head = prev


if __name__ == '__main__':
    s = LinkedList()
    s.append(5)
    s.append(6)
    s.append(4)
    s.append(9)
    s.append(100)
    s.append(56)

    s.insert(0, 10)
    s.insert(5, 43)
    s.insert(8, 99)
    s.print()

    s.delete(1)
    s.print()

    s.reverse()
    s.print()

    s.delete(3)
    s.print()

    s.reverse()
    s.print()
