import sys


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

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def print_helper(self, current_pointer, indent, last):
        if current_pointer != None:
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


# AVL Tree printing test case (uncomment to run).
# Przekopiujemy do maina żeby pokazać Chabko jak działa printowanie:
# root = None
# test_tree = AVL_Tree(root)
# nums = create_random_list(30)
# for num in nums:
#   root = myTree.insert_node(root, num)
# myTree.print_helper(root, "", True)
