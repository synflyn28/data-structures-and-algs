"""
This module contains an implementation of a Linked List in 
Python.
"""

class ListNode:
    """
    Node class for Linked List.
    """
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:
    """
    Linked List class.
    """

    def __init__(self):
        """
        Initialize Linked List.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get value an index-th node.
        """

        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head

        while index != 0:
            cur = cur.next
            index -= 1
        
        return cur.val

    def add_at_head(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        """
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
    
    def add_at_tail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
    
    def add_at_index(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals the length of linked list, the node will be appended to the end.
        If index is greater than the length, the node will not be inserted.
        """

        if index < 0 or index > self.size:
            return 
        elif index == 0:
            self.add_at_head(val)
        elif index == self.size:
            self.add_at_tail(val)
        else:
            cur = self.head

            while index != 0:
                cur = cur.next
                index -= 1
            
            new_node = ListNode(val)
            new_node.next = cur.next
            cur.next.prev = new_node
            cur.next = new_node
            new_node.prev = cur

            self.size += 1

    def delete_at_index(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        if index < 0 or index >= self.size:
            return 
        elif index == 0:
            cur = self.head.next
            if cur:
                cur.prev = None
            self.head = self.head.next
            self.size -= 1

            if self.size == 0:
                self.tail = None

        elif index == self.size - 1:
            cur = self.tail.prev

            if cur:
                cur.next = None
            self.tail = self.tail.prev
            self.size -= 1

            if self.size == 0:
                self.head = None
        else:
            cur = self.head

            while index-1 != 0:
                cur = cur.next
                index -= 1
            
            cur.next = cur.next.next # Overwite with node past the next node
            cur.next.prev = cur
            self.size -= 1


