class Heap:
    def __init__(self):
        self.storage = []

    def get_parent_idx(self, i):
        return (i-1)//2

# `insert` adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap
    def insert(self, value):
        # add value to the end of storage arr
        self.storage.append(value)
        # bubble up
        self._bubble_up(len(self.storage) - 1)


# `delete` removes and returns the 'topmost' value from the heap;
# this method needs to ensure that the heap property is maintained after the topmost element has been removed.

    def delete(self):
        pass

# `get_max` returns the maximum value in the heap _in constant time_.
    def get_max(self):
        pass

# `get_size` returns the number of elements stored in the heap.
    def get_size(self):
        pass

# `_bubble_up` moves the element at the specified index "up" the heap
# by swapping it with its parent if the parent's value is less than the value at the specified index.
    def _bubble_up(self, index):
        while index > 0:
            val_at_index = self.storage[index]
            parent_val = self.storage[self.get_parent_idx(index)]
            # check if it's value is bigger than parent
            if val_at_index > parent_val:
                # if it is, swap them
                self.storage[index], self.storage[self.get_parent_idx(
                    index)] = parent_val, val_at_index
            # if not, end
            else:
                break


# `_sift_down` grabs the indices of this element's children and determines which child has a larger value.
# If the larger child's value is larger than the parent's value, the child element is swapped with the parent.

    def _sift_down(self, index):
        pass


a = Heap()

a.insert(3)
print(a.storage)
a.insert(0)
print(a.storage)
a.insert(5)
print(a.storage)
