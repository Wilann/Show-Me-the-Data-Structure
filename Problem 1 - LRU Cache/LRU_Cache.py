class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  # least recently used pointer - "back" of DoublyLinkedList
        self.tail = None  # most recently used pointer - "front" of DoublyLinkedList

    # TODO 1
    def move_to_front(self, value):
        """
        Moves DoubleNode with particular value, value, to the front/tail of DoublyLinkedList

        :param value: Value to be moved
        :return: None
        """
        node = self.head

        if node.value != value:

            # Search for DoubleNode with value we want to move
            while node.next:
                # Adjust next pointer
                node = node.next

                if node.value == value:
                    break

        # Add designated node to LinkedList
        self.tail.next = node

        # Move head forward
        self.head = self.head.next

        # Move tail forward
        self.tail = self.tail.next


class Queue(LinkedList):
    def __init__(self):
        super().__init__()
        self.num_elements = 0

    def enqueue(self, value):
        """
        Appends a new value to front/tail

        :param value: Value to be added
        :return: None
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return

        self.tail.next = new_node  # add data to the next attribute of the tail (i.e. the end of the queue)
        self.tail = self.tail.next  # shift the tail (i.e., the back of the queue)

        self.num_elements += 1

    def dequeue(self):
        """
        Removes back/head element

        :return: None
        """
        if self.is_empty():
            return None

        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def __repr__(self):
        s = ''
        node = self.head

        while node.next:
            s += str(node.value) + ' '
            node = node.next

        s += str(self.tail.value)
        return s


class LRU_Cache(object):
    """
    Least Recently Used Cache Data Structure. \n
    LRU is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. \n
    All operations take O(1).
    """

    def __init__(self, capacity=5):
        """
        Initialize class variables

        :param capacity: size of cache
        """
        self.cache = dict()
        self.recently_used = Queue()  # keeps track of which keys were the most/least recently used
        self.capacity = capacity

    def get(self, key):
        """
        Retrieve item from provided key. Return -1 if nonexistent. \n
        Considered a use operation.

        :param key: key
        :return: item
        """

        # Cache Hit - entry is found
        if key in self.cache:
            # Get entry from cache
            entry = self.cache[key]

            # TODO 1: Move item to front/tail of recently_used
            self.recently_used.move_to_front(key)
            print("self.recently_used:", self.recently_used)

            # Return entry
            return entry

        # Catch Miss - entry isn't found
        return -1

    def set(self, key, value):
        """
        Set the value if the key is not present in the cache. \n
        If the cache is full, remove the oldest / least recently used item. Then insert the element. \n
        Considered a use operation.

        :param key: key
        :param value: value
        :return:
        """

        # If key isn't in the cache
        if key not in self.cache:
            # Add entry to cache
            self.cache[key] = value

            # Add item to front/tail of recently_used
            self.recently_used.enqueue(key)

            # TODO 2: Check and handle capacity - if full, delete oldest entry (back/head of recently_used)
            if self.recently_used.num_elements == self.capacity:
                oldest_entry = self.recently_used.dequeue()
                self.recently_used.enqueue(oldest_entry)

            print("self.recently_used:", self.recently_used)

            return

        # Key is in the cache
        self.cache[key] = value

        # TODO 1: Move item to front/tail of recently_used
        self.recently_used.move_to_front(key)
        print("self.recently_used:", self.recently_used)

    def __repr__(self):
        s = ''
        for key in self.cache:
            s += str(key) + ' ' + str(self.cache[key]) + ', '
        return s


our_cache = LRU_Cache(5)

print("--our_cache.set(1, 1)--")
our_cache.set(1, 1)
print("our_cache:", our_cache, '\n')

print("--our_cache.set(2, 2)--")
our_cache.set(2, 2)
print("our_cache:", our_cache, '\n')

print("--our_cache.set(3, 3)--")
our_cache.set(3, 3)
print("our_cache:", our_cache, '\n')

print("--our_cache.set(4, 4)--")
our_cache.set(4, 4)
print("our_cache:", our_cache, '\n')

print("--our_cache.get(1)--")
print(our_cache.get(1))  # returns 1
print("our_cache:", our_cache, '\n')

print("--our_cache.get(2)--")
print(our_cache.get(2))  # returns 2
print("our_cache:", our_cache, '\n')

print("--our_cache.get(9)--")
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache
print("our_cache:", our_cache, '\n')

print("--our_cache.set(5, 5)--")
our_cache.set(5, 5)
print("our_cache:", our_cache, '\n')

print("--our_cache.set(6, 6)--")
our_cache.set(6, 6)
print("our_cache:", our_cache, '\n')

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print("--our_cache.get(3)--")
print(our_cache.get(3))
print("our_cache:", our_cache, '\n')
