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
        if self.value == target:
            return True
        elif self.left == None or self.right == None:
            return False
        else:
            if target < self.value:
                return self.left.contains(target)
            else:
                return self.right.contains(target)


# `get_max` returns the maximum value in the binary search tree.


    def get_max(self):
        # if right child exists => there is a higher value in tree
        if self.right:
            # recursively loop until the most rightest node, which will have the highest value
            return self.right.get_max()
        # and then return it
        return self.value


# `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value.
# There is a myriad of ways to perform tree traversal; in this case any of them should work.

    def for_each(self, cb):
        # run the callback with node value
        cb(self.value)

        # if right node exist (we're not at the end of the tree), recursively run the fn again passing the cb in
        if self.right:
            return self.right.for_each(cb)
        # same as above
        if self.left:
            return self.left.for_each(cb)
