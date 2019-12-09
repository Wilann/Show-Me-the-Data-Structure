class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def is_empty(self):
        return self.size == 0

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

        # Increment size
        self.size += 1

    def __contains__(self, value):
        """
        Returns True if LinkedList has a node with value, other wise return False
        :param value:
        :return: True if Node(value) present in Linked List, False otherwise
        """
        if self.size == 0:
            return False

        node = self.head
        while node.next:
            if node.value == value:
                return True

            node = node.next

        # Last value
        return node.value == value


def union(llist_1, llist_2):
    """
    Returns the set of elements which are in either list

    :param llist_1: LinkedList
    :param llist_2: LinkedList
    :return: Union LinkedList
    """
    l = set()

    # Add all values of first list to set
    current = llist_1.head
    while current:
        l.add(current.value)
        current = current.next

    # Add all values of second list to set
    current = llist_2.head
    while current:
        l.add(current.value)
        current = current.next

    # Convert set to linked list
    union_list = LinkedList()
    for num in l:
        union_list.append(num)

    return union_list


def intersection(llist_1, llist_2):
    """
    Returns the set of elements which are in both lists

    :param llist_1: LinkedList
    :param llist_2: LinkedList
    :return: Intersection LinkedList
    """

    # Create set of llist_1
    list_3 = set()
    current = llist_1.head
    while current:
        list_3.add(current.value)
        current = current.next

    # Create set of llist_2
    list_4 = set()
    current = llist_2.head
    while current:
        list_4.add(current.value)
        current = current.next

    # Add values of llist_1 if they're in llist_2
    list_5 = [value for value in list_3 if value in list_4]

    # Create a linked list
    intersection_list = LinkedList()
    for num in list_5:
        intersection_list.append(num)

    return intersection_list


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Test Case 1:")
print("linked_list_1:", linked_list_1)
print("linked_list_2:", linked_list_2)
print("union(linked_list_1, linked_list_2):", union(linked_list_1, linked_list_2))
print("intersection(linked_list_1, linked_list_2):", intersection(linked_list_1, linked_list_2))
print()

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Test Case 2:")
print("linked_list_3:", linked_list_3)
print("linked_list_4:", linked_list_4)
print("union(linked_list_3, linked_list_4):", union(linked_list_3, linked_list_4))
print("intersection(linked_list_3, linked_list_4):", intersection(linked_list_3, linked_list_4))
