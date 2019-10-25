class Queue:

    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):
        if self.is_empty():
            self.front_index = -1  # resetting pointers
            self.next_index = 0
            return None

        # dequeue front element
        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return value

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.size() == 0


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
        self.capacity = capacity
        self.keysInserted = Queue(capacity)  # used to keep track of the oldest item

    def get(self, key):
        """
        Retrieve item from provided key. Return -1 if nonexistent. \n
        Considered a use operation.

        :param key: key
        :return: item
        """

        # Cache Hit - entry is found
        if key in self.cache:
            self.keysInserted.enqueue(key)
            return self.cache[key]

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

        # If cache is full
        if self.keysInserted.size == self.capacity:

            # remove oldest item
            self.cache.pop(self.keysInserted.dequeue())

            # insert element into cache
            self.cache[key] = value
            self.keysInserted.enqueue(key)

        # If key isn't present in the cache
        if self.get(key) == -1:

            # insert element into cache
            self.cache[key] = value
            self.keysInserted.enqueue(key)

    def __repr__(self):
        s = ''
        for key in self.cache:
            s += str(key) + ' ' + str(self.cache[key]) + ', '
        return s


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache)

print("our_cache.get(1):", our_cache.get(1))  # returns 1
print("our_cache.get(2):", our_cache.get(2))  # returns 2
print("our_cache.get(9):", our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
print(our_cache)


our_cache.set(6, 6)
print(our_cache)

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print("our_cache.get(3):", our_cache.get(3))
