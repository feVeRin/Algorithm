class Node:
    def __init__(self, val=None, left=None, right=None, parent=None, color='B'):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color


class RBT:
    def __init__(self):
        self.NIL = Node()
        self.root = self.NIL

    def insert(self, val):
        new = Node(val, self.NIL, self.NIL, None, 'R')

        parent = None
        cur = self.root

        while cur != self.NIL:
            parent = cur
            if new.val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        new.parent = parent

        if parent is None:
            self.root = new
        elif new.val < parent.val:
            parent.left = new
        else:
            parent.right = new

        if new.parent is None:
            new.color = 'B'
            return

        if new.parent.parent is None:
            return

        self._insert(new)

    def _insert(self, node):
        while node.parent.color == 'R':
            if node.parent == node.parent.parent.right:
                ucl = node.parent.parent.left
                if ucl.color == 'R':
                    ucl.color = 'B'
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._Rrotate(node)
                    else:
                        node.parent.color = 'B'
                        node.parent.parent.color = 'R'
                        self._Lrotate(node.parent.parent)
            else:
                ucl = node.parent.parent.right

                if ucl.color == 'R':
                    ucl.color = 'B'
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._Lrotate(node)

                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self._Rrotate(node.parent.parent)

            if node == self.root:
                break

        self.root.color = 'B'

    def _Lrotate(self, node):
        tmp = node.right
        node.right = tmp.left

        if tmp.left != self.NIL:
            tmp.left.parent = node

        tmp.parent = node.parent

        if node.parent is None:
            self.root = tmp
        elif node == node.parent.left:
            node.parent.left = tmp
        else:
            node.parent.right = tmp

        tmp.left = node
        node.parent = tmp

    def _Rrotate(self, node):
        tmp = node.left
        node.left = tmp.right

        if tmp.right != self.NIL:
            tmp.right.parent = node

        tmp.parent = node.parent

        if node.parent is None:
            self.root = tmp
        elif node == node.parent.right:
            node.parent.right = tmp
        else:
            node.parent.left = tmp

        tmp.right = node
        node.parent = tmp


def inorder(node):  # NLR
    if node.val is None:
        return

    inorder(node.left)
    print(node.val)
    inorder(node.right)


if __name__ == '__main__':
    rbt = RBT()
    num = [50, 30, 24, 5, 28, 45, 98, 52, 60]
    for i in num:
        rbt.insert(i)

    inorder(rbt.root)
