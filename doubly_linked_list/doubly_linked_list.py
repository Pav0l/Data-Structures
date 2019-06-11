"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """add_to_head replaces the head of the list with a new value that is passed in"""

    def add_to_head(self, value):
        if self.head == None:
            # if head doesnt exist yet, create it
            self.head = ListNode(value)
            self.tail = ListNode(value)
        else:
            # insert value before head
            self.head.insert_before(value)
            # make new head the inserted value
            self.head = self.head.prev
        self.length += 1

    """remove_from_head removes the head node and returns the value stored in it"""

    def remove_from_head(self):
        if self.head == None:
            return None
        else:
            if self.length == 1:
                self.tail = None
            # save current head value to return
            value = self.head.value
            # save next node after head
            next_head = self.head.next
            # delete current head
            self.head.delete()
            # make previously next node new head
            self.head = next_head
            self.length -= 1
            return value

    """add_to_tail replaces the tail of the list with a new value that is passed in"""

    def add_to_tail(self, value):
        if self.tail == None:
            # if tail doesnt exist yet, create it
            self.head = ListNode(value)
            self.tail = ListNode(value)
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    """remove_from_tail removes the tail node and returns the value stored in it"""

    def remove_from_tail(self):
        if self.tail == None:
            return None
        else:
            if self.length == 1:
                self.head = None
            value = self.tail.value
            new_tail = self.tail.prev
            self.tail.delete()
            self.tail = new_tail
            self.length -= 1
            return value

    """move_to_front takes a reference to a node in the list and moves it to the front of the list, shifting all other list nodes down"""

    def move_to_front(self, node):
        if node == self.tail:
            self.tail = self.tail.prev

        self.head.insert_before(node.value)
        self.head = self.head.prev

        return self.head

    """move_to_end takes a reference to a node in the list and moves it to the end of the list, shifting all other list nodes up"""

    def move_to_end(self, node):
        if node == self.head:
            self.head = self.head.next

        self.tail.insert_after(node.value)
        self.tail = self.tail.next

        return self.tail

    """delete takes a reference to a node in the list and removes it from the list. The deleted node's previous and next pointers should point to each afterwards"""

    def delete(self, node):
        if self.head == node:
            self.head = node.next

        if self.tail == node:
            self.tail = node.prev

        node.delete()
        self.length -= 1

    """get_max returns the maximum value in the list"""

    def get_max(self):
        max_val = self.head.value
        current_head = self.head
        while current_head:
            if not max_val or current_head.value > max_val:
                max_val = current_head.value
            # traverse thru the list.
            current_head = current_head.next
        return max_val
