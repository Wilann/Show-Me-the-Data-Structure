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

        return False


def union(llist_1, llist_2):
    """
    Returns the set of elements which are in either list

    :param llist_1: LinkedList
    :param llist_2: LinkedList
    :return: Union LinkedList
    """
    union_list = LinkedList()

    # Populate linked list with unique values llist_1
    node = llist_1.head
    while node.next:

        # If the node's value isn't in the linked list
        if node.value not in union_list:
            union_list.append(node.value)

        node = node.next

    # Account for last value of llist_1
    if node.value not in union_list:
        union_list.append(node.value)

    # Populate linked list with unique values llist_2
    node = llist_2.head
    while node.next:

        # If the node's value isn't in the linked list
        if node.value not in union_list:
            union_list.append(node.value)

        node = node.next

    # Account for last value of llist_2
    if node.value not in union_list:
        union_list.append(node.value)

    return union_list


# TODO
def intersection(llist_1, llist_2):
    """
    Returns the set of elements which are in both lists

    :param llist_1: LinkedList
    :param llist_2: LinkedList
    :return: Intersection LinkedList
    """
    intersection_list = LinkedList()

    # Traverse llist_1
    node = llist_1.head
    while node.next:

        # If node's value is in llist_2 and isn't already in intersection_list (checking for duplicates)
        if node.value in llist_2 and node.value not in intersection_list:
            intersection_list.append(node.value)

        node = node.next

    # Account for last value of llist_1
    if node.value in llist_2 and node.value not in intersection_list:
        intersection_list.append(node.value)

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
