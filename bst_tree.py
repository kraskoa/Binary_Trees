import random


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

    def print_tree(self, root, visible_layers=6):
        print()
        print("Binary Search Tree")
        print("Visible nodes layers: ", visible_layers)
        print()
        self.print_tree_util(root, 0, visible_layers)

    def print_tree_util(self, root, space, visible_layers, recursion=1):
        if not root:
            return
        space += 5
        recursion += 1
        if recursion <= visible_layers:
            self.print_tree_util(root.right, space, visible_layers, recursion)
        for _ in range(5, space):
            print(end=" ")
        if root.parent is None:
            print("P:", end="")
            print(root.key)
        elif root.parent.key > root.key:
            print("L:", end="")
            print(root.key)
        elif root.parent.key < root.key:
            print("R:", end="")
            print(root.key)
        if recursion <= visible_layers:
            self.print_tree_util(root.left, space, visible_layers, recursion)


def main():
    root = Node(25)
    tree = BST_tree(root)
    for i in range(50):
        tree.insert(root, random.randint(1, 100))
    tree.print_tree(root)


if __name__ == "__main__":
    main()
