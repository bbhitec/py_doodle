##!/usr/bin/env python
'''
    @author [mst]
    @file   linked_lists.py

    linked lists doodles in python
    [wip] make a menu with insertion and deletion etc
    - use or omition of the of super class
    - iterative and recursive reversal
    - used in leetcode 206

    features, changelog:
    -2022.11: -initial draft

    @version 0.1 2022.05
'''

class className():
    '''docstring comment
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
     '''
    def method1(self):
        return

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
      self.headval = None

    # construct from an array
    def __init__(self, nums):
        if not nums:
            return None
        self.headval = ListNode(nums[0])
        p = self.headval
        for n in nums[1::]:
            new_node = ListNode(n)
            p.next = new_node
            p = p.next

    def printList(self):
        lst = self.headval
        while lst:
            print(f"{lst.val} -> ", end='')
            lst = lst.next
        print("")

    # [demo] recursive list reversal
    def reverseListRec(self, head: ListNode):
        # stopping condition. we use next.nxt so we have to check it is valid
        if head is None or head.next is None:
            return head

        # treat rest of list
        rest = self.reverseList(head.next)

        # treat current node
        head.next.next = head
        head.next = None
        return rest


    # [demo] iterative three-pointer list reversal
    def reverseList(self):
        prev = None
        curr = self.headval

        while curr is not None:
            # XOR method from: https://www.geeksforgeeks.org/iteratively-reverse-a-linked-list-using-only-2-pointers/
            # # This expression evaluates from left to right
            # # current->next = prev, changes the link from
            # # next to prev node
            # # prev = current, moves prev to current node for
            # # next reversal of node
            # # This example of list will clear it more 1->2
            # # initially prev = 1, current = 2
            # # Final expression will be current = 1, prev = 2
            # next, current.next = current.next, prev
            # prev, current = current, next

            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.headval = prev

    def insert(self, n):
        p = self.headval

        while (p is not None) and (p.next is not None) and (p.next.val < n):
            p = p.next

        new_node = ListNode(n, p.next)
        p.next = new_node


    # used in leetcode 203
    def remove(self, n):
        if self.headval.val == n:
            self.headval = self.headval.next
            return

        prev = self.headval
        curr = self.headval.next

        while curr is not None:
            if curr.val == n:
                # the actual deletion (omission),
                # we can return here if only a single deletion is required
                prev.next = curr.next
                # return
            else:
                prev = curr
            curr = curr.next




################## DRIVER
def main():

    print ("[mst] linked lists doodle")

    arr = [1,2,3,7]
    print("creating")
    list1 = LinkedList(arr)
    list1.printList()

    print("inserting")
    list1.insert(6)
    list1.insert(3)
    list1.printList()

    # print("reversing")
    # list1.reverseList()
    # list1.printList()

    print("removing " + "3")
    list1.remove(3)
    list1.printList()





if __name__ == ("__main__"):
    main()
