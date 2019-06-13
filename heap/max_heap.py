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
        heap = self.storage[0]
        last = self.storage[-1]
        # swap first with last element in list
        self.storage[0], self.storage[-1] = last, heap
        # remove last (previous heap) element
        print(f'*** DELETING {self.storage[-1]} from {self.storage} ***')
        self.storage.pop()
        print(f'*** THIS IS LEFT {self.storage} ***')

        # sift down the tree and swap any items that are not in right order
        self._sift_down(0)


# `get_max` returns the maximum value in the heap _in constant time_.

    def get_max(self):
        return self.storage[0]

# `get_size` returns the number of elements stored in the heap.
    def get_size(self):
        return len(self.storage)

# `_bubble_up` moves the element at the specified index "up" the heap
# by swapping it with its parent if the parent's value is less than the value at the specified index.
    def _bubble_up(self, index):
        # run "infinite" loop for any index bigger than root element
        # the while loop will break if parent value is bigger than value at index
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
        print(f'Storage: {self.storage}\n')

        if index > len(self.storage)-1:
            return
        # get parent and children
        parent = self.storage[index]
        left_idx = 2 * index + 1
        right_idx = 2 * index + 2

        if left_idx > len(self.storage) - 1:
            # no child does exist
            return
        elif right_idx > len(self.storage) - 1:
            # right child does not exist
            left_val = self.storage[left_idx]
            right_val = None
        else:
            # both childs exist
            left_val = self.storage[left_idx]
            right_val = self.storage[right_idx]

        # compare the parent value with value of left child
        # if left child is bigger than parent
        if left_val > parent:
            # compare left child with right child
            # if left child is bigger than right child
            if right_val is None or left_val > right_val:
                # swap left child with parent
                print(f'before: {self.storage}')
                print(
                    f'left val: {self.storage[left_idx]}, right val: {right_val}, parent: {self.storage[index]}')
                self.storage[left_idx], self.storage[index] = parent, self.storage[left_idx]
                # and call this function again with index of parent
                print(f'\nafter: {self.storage}')
                print(
                    f'left val: {self.storage[left_idx]}, right val: {right_val}, parent: {self.storage[index]}\n')
                self._sift_down(left_idx)
            else:
                print(f'before: {self.storage}')
                print(
                    f'left val: {self.storage[left_idx]}, right val: {right_val}, parent: {self.storage[index]}')
                # if right child is bigger than left child
                # swap right child with parent
                self.storage[right_idx], self.storage[index] = parent, self.storage[right_idx]
                print(f'\nafter: {self.storage}')
                print(
                    f'left val: {self.storage[left_idx]}, right val: {right_val}, parent: {self.storage[index]}\n')
                # and call this function again with index of parent
                self._sift_down(right_idx)

        # if parent is bigger than left child, compare parent with right child
        elif right_val is not None or right_val > parent:
            # if right child is bigger than parent
            # swap right child with parent
            print(f'before: {self.storage}')
            print(
                f'left val: {self.storage[left_idx]}, right val: {right_val}, parent: {self.storage[index]}')
            self.storage[right_idx], self.storage[index] = parent, self.storage[right_idx]
            # and call this function again with index of parent
            print(f'\nafter: {self.storage}')
            print(
                f'left val: {self.storage[left_idx]}, right val: {right_val}, parent: {self.storage[index]}\n')
            self._sift_down(right_idx)

        # else end
        else:
            return


# a = Heap()

# a.insert(3)
# a.insert(0)
# a.insert(5)
# a.insert(7)
# a.insert(12)
# a.insert(4)
# a.insert(9)
# a.insert(1)
# print(a.storage)
# a._sift_down(5)
