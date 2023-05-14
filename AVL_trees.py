class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, root, val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        return self.balance(root)

    def balance(self, root):
        if self.get_balance(root) > 1:
            if self.get_balance(root.left) < 0:
                root.left = self.left_rotate(root.left)
            root = self.right_rotate(root)
        elif self.get_balance(root) < -1:
            if self.get_balance(root.right) > 0:
                root.right = self.right_rotate(root.right)
            root = self.left_rotate(root)
        return root

    def left_rotate(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        new_root.height = max(self.get_height(new_root.left), self.get_height(new_root.right)) + 1
        return new_root

    def right_rotate(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        new_root.height = max(self.get_height(new_root.left), self.get_height(new_root.right)) + 1
        return new_root

    def get_height(self, root):
        if root is None:
            return 0
        return root.height

    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def inorder_traverse(self, root, res):
        if root is None:
            return
        self.inorder_traverse(root.left, res)
        res.append(root.val)
        self.inorder_traverse(root.right, res)


def test_AVL_by_sorting_random_numbers():
    import random
    random.seed(0)
    arr = [random.randint(0, 1000) for _ in range(1000)]
    tree = AVLTree()
    for num in arr:
        tree.insert(num)
    res = []
    tree.inorder_traverse(tree.root, res)
    assert res == sorted(arr)
    print('test passed')


def check_AVL_for_balance():
    tree = AVLTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert(25)
    assert tree.root.val == 30
    assert tree.root.left.val == 20
    assert tree.root.right.val == 40
    assert tree.root.left.left.val == 10
    assert tree.root.left.right.val == 25
    assert tree.root.right.right.val == 50
    print('test passed')


if __name__ == '__main__':
    test_AVL_by_sorting_random_numbers()
    check_AVL_for_balance()