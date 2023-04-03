import sys
from create_list import create_list


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree:
    def insert_node(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance_factor = self.get_balance(root)
        if balance_factor > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_factor < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def left_rotate(self, pivot):
        r_subtree = pivot.right
        left_part = r_subtree.left
        r_subtree.left = pivot
        pivot.right = left_part
        pivot.height = 1 + max(
            self.get_height(pivot.left), self.get_height(pivot.right)
        )
        r_subtree.height = 1 + max(
            self.get_height(r_subtree.left), self.get_height(r_subtree.right)
        )
        return r_subtree

    def right_rotate(self, pivot):
        l_subtree = pivot.left
        right_part = l_subtree.right
        l_subtree.right = pivot
        pivot.left = right_part
        pivot.height = 1 + max(
            self.get_height(pivot.left), self.get_height(pivot.right)
        )
        l_subtree.height = 1 + max(
            self.get_height(l_subtree.left), self.get_height(l_subtree.right)
        )
        return l_subtree

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def print_helper(self, current_pointer, indent, last):
        if current_pointer:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(current_pointer.key)
            self.print_helper(current_pointer.left, indent, False)
            self.print_helper(current_pointer.right, indent, True)

    def find_node(self, root, key):
        if not root:
            return None
        elif root.key == key:
            return key
        elif key < root.key:
            return self.find_node(root.left, key)
        elif key > root.key:
            return self.find_node(root.right, key)


if __name__ == "__main__":
    root = None
    test_tree = AVL_Tree()
    nums = create_list(30)
    for num in nums:
        root = test_tree.insert_node(root, num)
    test_tree.print_helper(root, "", True)
