class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None  # least recently used pointer - "back" of DoublyLinkedList
        self.tail = None  # most recently used pointer - "front" of DoublyLinkedList

    def remove(self, node):
        """
        Removes node

        :param node: Node to be removed
        :return: None
        """
        # If the head is the node we want to remove
        if self.head.value == node.value:
            # Save node to advance head to
            next_node = self.head.next

            # Configure pointers
            next_node.previous = None
            self.head.next = None

            # Advance head
            self.head = next_node

        # If the tail is the node we want to remove
        elif self.tail.value == node.value:
            self.tail = self.tail.previous
            self.tail.next = None

        # General case
        else:
            previous = node.previous
            next = node.next
            previous.next = next
            next.previous = previous

    def remove_temp(self, value):
        """
        Removes and returns Node with value

        :param value: Value to be removed
        :return: value
        """

        # If the head is the node we need to remove
        if self.head.value == value:
            temp_value = self.head.value

            # Advance head
            self.head = self.head.next

            return temp_value

        # Find node to remove
        node = self.head
        while node.next is not None:
            if node.next.value == value:
                break

            # Advance node
            node = node.next

        # Adjust surrounding pointers
        node.next = node.next.next

        return node.next.value


class Queue(LinkedList):
    def __init__(self):
        super().__init__()
        self.num_elements = 0

    def enqueue(self, node):
        """
        Appends a new value to front/tail

        :param value: Value to be added
        :return: None
        """
        new_node = node

        # If the Queue has no Nodes
        if self.head is None and self.tail is None:
            # Set head and tail to new_node
            self.head = new_node
            self.tail = self.head

        # The Queue already has at least one Node
        else:
            # Add new_node to the end of the queue abd configure pointers
            self.tail.next = new_node
            new_node.previous = self.tail

            # Advance tail
            self.tail = self.tail.next

    def dequeue(self):
        """
        Removes back/head element

        :return: None
        """
        # If the Queue is empty
        if self.is_empty():
            return None

        # Save value in a variable
        value = self.head.value

        # Advance head
        self.head = self.head.next

        # Remove head's previous pointer
        self.head.previous = None

        # Decrement num_elements
        # self.num_elements -= 1

        # Return least recently used value
        return value

    def increment_num_elements(self):
        """
        Increment num_elements

        :return: None
        """
        self.num_elements += 1

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def __repr__(self):
        s = ''
        node = self.head

        while node is not None:
            s += str(node.value) + ' '
            node = node.next

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
        self.cache = dict()  # Mapping of [key => Node(value)]
        self.recently_used = Queue()  # Keeps track of which keys were the most/least recently used
        self.capacity = capacity

    def get(self, key):
        """
        Retrieve item from provided key. Return -1 if nonexistent. \n
        Considered a use operation.

        :param key: key
        :return: item
        """

        # If key is in cache (Cache Hit)
        if key in self.cache:
            # Get entry from cache
            entry = self.cache[key].value

            # Get node from cache
            node = self.cache[key]

            # Remove node from recently_used
            self.recently_used.remove(node)

            # Add node to front/tail of recently_used
            self.recently_used.enqueue(node)

            print("self.recently_used:", self.recently_used)

            # Return entry
            return entry

        # Key isn't in cache (Catch Miss)
        return -1

    def set(self, key=None, value=None):
        """
        Set the value if the key is not present in the cache. \n
        If the cache is full, remove the oldest / least recently used item. Then insert the element. \n
        Considered a use operation.

        :param key: key
        :param value: value
        :return:
        """

        # Edge cases
        if key is None or value is None:
            return
        elif self.capacity == 0:
            print("Can't perform operations on a 0 capacity cache")
            return

        # If key isn't in the cache
        if key not in self.cache:
            # Check and handle capacity - if full, delete oldest entry (back/head of recently_used)
            if self.recently_used.num_elements == self.capacity:
                # Remove oldest entry from recently_used
                oldest_entry = self.recently_used.dequeue()

                # Remove equivalent key from cache
                del self.cache[oldest_entry]

            # Create Node instance
            node = Node(value)

            # Add entry to cache
            self.cache[key] = node

            # Add item to front/tail of recently_used
            self.recently_used.enqueue(node)

            # Increment number of elements
            self.recently_used.increment_num_elements()

            print("self.recently_used:", self.recently_used)

        # Key is in the cache
        else:
            # Get node from cache
            node = self.cache[key]

            # Remove node from recently_used
            self.recently_used.remove(node)

            # Add node to front/tail of recently_used
            self.recently_used.enqueue(node)

            print("self.recently_used:", self.recently_used)

    def __repr__(self):
        s = ''
        for key in self.cache:
            s += str(key) + ' ' + 'Node(' + str(self.cache[key].value) + '), '
        return s


# Edge test cases for empty cache
our_cache = LRU_Cache(0)
print("our_cache:", our_cache, '\n')

print("--our_cache.set(1, 1)--")
our_cache.set(1, 1)  # Can't perform operations on a 0 capacity cache
print("our_cache:", our_cache, '\n')

print("--our_cache.get(1)--")
print("our_cache.get(1):", our_cache.get(1))  # returns -1
print("our_cache:", our_cache, '\n')

# General test cases
our_cache = LRU_Cache(5)
print("our_cache:", our_cache, '\n')

print("--our_cache.set(, )--")
our_cache.set()  # No return
print("our_cache:", our_cache, '\n')

print("--our_cache.set(1, 1)--")
our_cache.set(1, 1)  # No return
print("our_cache:", our_cache, '\n')

print("--our_cache.set(2, 2)--")
our_cache.set(2, 2)  # No return
print("our_cache:", our_cache, '\n')

print("--our_cache.set(3, 3)--")
our_cache.set(3, 3)  # No return
print("our_cache:", our_cache, '\n')

print("--our_cache.set(4, 4)--")
our_cache.set(4, 4)  # No return
print("our_cache:", our_cache, '\n')

print("--our_cache.get(1)--")
print("our_cache.get(1):", our_cache.get(1))  # returns 1
print("our_cache:", our_cache, '\n')

print("--our_cache.get(2)--")
print("our_cache.get(2):", our_cache.get(2))  # returns 2
print("our_cache:", our_cache, '\n')

print("--our_cache.get(9)--")
print("our_cache.get(9):", our_cache.get(9))  # returns -1 because 9 is not present in the cache
print("our_cache:", our_cache, '\n')

print("--our_cache.set(5, 5)--")
our_cache.set(5, 5)  # No return
print("our_cache:", our_cache, '\n')

print("--our_cache.set(6, 6)--")
our_cache.set(6, 6)  # No return
print("our_cache:", our_cache, '\n')

print("--our_cache.get(3)--")
print("our_cache.get(3):", our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print("our_cache:", our_cache, '\n')
