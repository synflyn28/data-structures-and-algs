"""
This script contains the implementation of a reversing a linked list.
"""

class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        """
        Reverse a linked list. Starts at a Node instead of a LinkedList instance
        since it has to iterate through all the node next values.
        """

        # Three pointers used to iterate and reverse the linked list.
        pre = None
        cur = head
        suc = None

        while cur:
            suc = cur.next
            cur.next = pre # *Switches the reference of the current node to reverse the LinkedList*
            
            # Move pre and cur pointers one step forward.
            pre = cur
            cur = suc
            # No succeeding move needed because suc is assigned next value at beginning of loop.

            return pre # Return preceding node when cur is None at the end of the LinkedList.
