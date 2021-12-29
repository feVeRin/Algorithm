class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left:
                self._insert(node.left, val)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = Node(val)

    def search(self, val):
        cur = self.root

        while cur:
            if cur.val == val:
                return cur
            elif val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        return None
    
    def remove(self, val):
        self.root = self._remove(self.root, val)

    def _remove(self, node, val):
        if node is None:
            return None

        if val < node.val:
            node.left = self._remove(node.left, val)
            return node
        elif val > node.val:
            node.right = self._remove(node.right, val)
            return node
        else:
            if (node.left is None) and (node.right is None):
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                tmp = self._min(node.right)
                node.val = tmp.val
                node.right = self._remove(node.right, val)
                return node

    @staticmethod
    def _min(cur):
        while cur:
            cur = cur.left
        return cur


def inorder(node):  # NLR
    if node is None:
        return

    inorder(node.left)
    print(node.val)
    inorder(node.right)


if __name__ == '__main__':
    bst = BST()
    num = [50, 30, 24, 5, 28, 45, 98, 52, 60]
    for i in num:
        bst.insert(i)

    inorder(bst.root)

    bst.remove(5)
    print()
    print(bst.search(5))
    print()

    inorder(bst.root)
