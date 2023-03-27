class BST_tree:
    def __inti__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def search(self, key):
        if self.root == key:
            return True
        elif self.root > key:
            if self.left:
                return self.left.search(key)
            else:
                return False
        else:
            if self.right:
                return self.right.search(key)
            else:
                return False

    def insert(self, key):
        if self.root == key:
            return False
        elif self.root > key:
            if self.left:
                return self.left.insert(key)
            else:
                self.left = BST_tree(key)
                return True
        else:
            if self.right:
                return self.right.insert(key)
            else:
                self.right = BST_tree(key)
                return True
