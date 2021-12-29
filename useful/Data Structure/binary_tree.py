class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(node):  # LNR
    if node is None:
        return

    print(node.val)
    preorder(node.left)
    preorder(node.right)


def inorder(node):  # NLR
    if node is None:
        return

    inorder(node.left)
    print(node.val)
    inorder(node.right)


def postorder(node):  # LRN
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.val)


if __name__ == '__main__':
    root = BinaryTree(6)
    root.left = BinaryTree(2)
    root.right = BinaryTree(7)
    root.left.left = BinaryTree(1)
    root.left.right = BinaryTree(4)
    root.left.right.left = BinaryTree(3)
    root.left.right.right = BinaryTree(5)
    root.right.right = BinaryTree(9)
    root.right.right.left = BinaryTree(8)

    preorder(root)
    print()
    inorder(root)
    print()
    postorder(root)
