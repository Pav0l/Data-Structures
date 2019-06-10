class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.size = 0
        # entry point of the queue (back of queue) == HEAD of Node list
        self.storage = Node()

    # enqueue should add an item to the back of the queue
    def enqueue(self, item):
        # no items in storage => first item in queue
        if not self.storage.value:
            new_node = Node(item)
            self.storage = new_node
        # if there are other items in the queue
        # add new node and give it ref to previous Head node
        else:
            # create new Node to add to queue
            new_node = Node(item)
            # connect new Node to previous HEAD node
            new_node.next_node = self.storage
            # make new Node new HEAD node
            self.storage = new_node

        # increase the size of the queue
        self.size += 1

    # dequeue should remove and return an item from the front of the queue
    def dequeue(self):
        # if empty Node List, return None
        if self.size == 0:
            return None
        else:
            current_node = self.storage

            # print(f'Current node value: {current_node.value}')

            # loop through the Node list untill you find a Node which next node is None (TAIL node)
            while current_node.next_node:

                # print(f'Next node: {current_node.next_node}')
                # print(f'Next node value: {current_node.next_node.value}')

                current_node = current_node.next_node
            # when you get to the TAIL node, save its value in a placeholder var
            value = current_node.value
            # remove the TAIL node
            current_node.value = None
            current_node.next_node = None

            # decrease the size of the queue
            self.size -= 1
            # return dequeued value
            return value

    # len returns the number of items in the queue
    def len(self):
        return self.size


q = Queue()
print(f'first len: {q.len()} ...should be 0')
q.enqueue(10)
print(f'added 1 item: {q.len()} ..should be 1')
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(f'add 3 more items: {q.len()} ..should be 4')
print(f'Removing: {q.dequeue()}')
print(f'removed 1 item: {q.len()} ..should be 3')
print(q.dequeue())
print(f'removed 1 item: {q.len()} ..should be 2')


class Queue_Array:
    def __init__(self):
        self.size = 0
        self.storage = []

    def enqueue(self, item):
        self.storage.insert(0, item)

    def dequeue(self):
        if len(self.storage) == 0:
            return None
        else:
            return self.storage.pop()

    def len(self):
        return len(self.storage)
