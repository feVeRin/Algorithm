class MinHeap:
    def __init__(self):
        self.arr = [None]

    def _swap(self, x, y):
        self.arr[x], self.arr[y] = self.arr[y], self.arr[x]

    def insert(self, val):
        self.arr.append(val)
        self.up_heap()

    def up_heap(self):
        idx = len(self.arr) - 1
        parent = idx // 2

        while parent > 0:
            if self.arr[idx] < self.arr[parent]:
                self._swap(parent, idx)
                idx = parent
                parent = idx // 2
            else:
                break

    def extract(self):
        val = self.arr[1]
        self._swap(1, len(self.arr)-1)
        self.arr.pop()
        self.down_heap(1)
        return val

    def down_heap(self, idx):
        left = 2*idx
        right = 2*idx + 1
        _min = idx

        if left <= len(self.arr)-1 and self.arr[left] < self.arr[_min]:
            _min = left

        if right <= len(self.arr)-1 and self.arr[right] < self.arr[_min]:
            _min = right

        if _min != idx:
            self._swap(idx, _min)
            self.down_heap(_min)


class MaxHeap:
    def __init__(self):
        self.arr = [None]

    def _swap(self, x, y):
        self.arr[x], self.arr[y] = self.arr[y], self.arr[x]

    def insert(self, val):
        self.arr.append(val)
        self.up_heap()

    def up_heap(self):
        idx = len(self.arr) - 1
        parent = idx // 2

        while parent > 0:
            if self.arr[idx] > self.arr[parent]:
                self._swap(parent, idx)
                idx = parent
                parent = idx // 2
            else:
                break

    def extract(self):
        val = self.arr[1]
        self._swap(1, len(self.arr)-1)
        self.arr.pop()
        self.down_heap(1)
        return val

    def down_heap(self, idx):
        left = 2*idx
        right = 2*idx + 1
        _max = idx

        if left <= len(self.arr)-1 and self.arr[_max] < self.arr[left]:
            _max = left

        if right <= len(self.arr)-1 and  self.arr[_max] < self.arr[right]:
            _max = right

        if _max != idx:
            self._swap(idx, _max)
            self.down_heap(_max)


if __name__ == '__main__':
    mhp = MinHeap()
    mhp2 = MaxHeap()

    num = [50, 30, 24, 5, 28, 45, 98, 52, 60]
    for i in num:
        mhp.insert(i)
        mhp2.insert(i)

    print(mhp.arr)
    print(mhp2.arr)

    print(mhp.extract())
    print(mhp2.extract())

    print(mhp.arr)
    print(mhp2.arr)
