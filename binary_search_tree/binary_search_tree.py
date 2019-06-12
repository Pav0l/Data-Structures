class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# `insert` adds the input value to the binary search tree,
# adhering to the rules of the ordering of elements in a binary search tree.
    def insert(self, value):
        # check if the new value is less then current value
        if value < self.value:
            # check if there is a current left child
            if self.left == None:
                # if there is no left child currently, place a new node
                self.left = BinarySearchTree(value)
            else:
                # otherwise repeat the process untill you get to the last leaf
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

# `contains` searches the binary search tree for the input value,
# returning a boolean indicating whether the value exists in the tree or not.
    def contains(self, target):
        pass


# `get_max` returns the maximum value in the binary search tree.

    def get_max(self):
        pass


# `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value.
# There is a myriad of ways to perform tree traversal; in this case any of them should work.

    def for_each(self, cb):
        pass
