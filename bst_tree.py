class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BST_tree:
    def __init__(self, root: Node):
        self.root = root

    def search(self, root, key):
        if not root:
            return None
        elif root.key == key:
            return key
        elif key < root.key:
            return self.search(root.left, key)
        elif key > root.key:
            return self.search(root.right, key)

    def insert(self, root, key):
        if not root:
            root = Node(key)
        elif key < root.key:
            if not root.left:
                new_node = Node(key)
                new_node.parent = root
                root.left = new_node
            else:
                self.insert(root.left, key)
        elif key > root.key:
            if not root.right:
                new_node = Node(key)
                new_node.parent = root
                root.right = new_node
            else:
                self.insert(root.right, key)

    def remove(self, root, key):
        if not root:
            return None
        elif key < root.key:
            self.remove(root.left, key)
        elif key > root.key:
            self.remove(root.right, key)
        else:
            if root.left and root.right:
                min_node = self.find_min(root.right)
                root.key = min_node.key
                self.remove(root.right, min_node.key)
            elif root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                root = None

    def find_min(self, root):
        if not root:
            return None
        while root.left:
            root = root.left
        return root

    def print_tree(self, root):
        if not root:
            return None
        print(root.key)
        self.print_tree(root.left)
        self.print_tree(root.right)


def main():
    root = Node(5)
    tree = BST_tree(root)
    tree.insert(root, 3)
    tree.insert(root, 2)
    tree.insert(root, 4)
    tree.insert(root, 7)
    tree.insert(root, 6)
    tree.insert(root, 8)
    tree.print_tree(root)


if __name__ == "__main__":
    main()
