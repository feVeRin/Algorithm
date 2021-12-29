import collections


class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = collections.defaultdict(Node)

    def _hash(self, key):
        return key % self.size

    def push(self, key, val):
        idx = self._hash(key)

        if self.table[idx].val is None:
            self.table[idx] = Node(key, val)
            return

        cur = self.table[idx]
        while cur.next:
            cur = cur.next

        cur.next = Node(key, val)

    def pull(self, key):
        idx = self._hash(key)
        tmp = []

        if self.table[idx].val is None:
            return -1

        cur = self.table[idx]
        while cur:
            tmp.append(cur.val)
            cur = cur.next

        return tmp

    def remove(self, key):
        idx = self._hash(key)
        prev = None

        if self.table[idx].val is None:
            return

        cur = self.table[idx]
        if cur.next is None:
            cur.val = None
            return

        while cur.next:
            prev = cur
            cur = cur.next

        prev.next = prev.next.next


if __name__ == '__main__':
    ht = HashTable(8)
    ht.push(1, 1)
    ht.push(1, 100)
    ht.push(1, 5)
    ht.push(1, 700)
    ht.push(2, 10)
    ht.push(3, 50)
    print(ht.pull(1))
    print(ht.pull(2))
    print(ht.pull(3))

    ht.remove(1)
    ht.remove(1)
    ht.remove(1)
    ht.remove(1)
    print(ht.pull(1))

    ht.push(1, 500)
    print(ht.pull(1))

    ht.push(2, 1)
    print(ht.pull(2))
    ht.remove(2)
    print(ht.pull(2))
