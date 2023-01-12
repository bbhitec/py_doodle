##!/usr/bin/env python
'''
    @author [mst]
    @file   tree.py
    @brief  Binary tree implementations and utils
    
    gains:
    -python basic classes, syntax

    features, changelog:
    -2023.01: -initial

    @version 0.1 2023.01
'''

################## DECL_IMPL

# Definition for a binary tree node. (taken from leetcode problems)
class TreeNode:
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(f"{self.val} ", end='')
        if self.right:
            self.right.print_inorder()
        return

    # insert single node
    def insert(self, x):
        # empty node insertion
        if self.val == -1:
            self.val = x
            return

        # bst insertions
        if x <= self.val:
            if self.left:
                self.left.insert(x)
            else:
                self.left = TreeNode(x)
        else:
            if self.right:
                self.right.insert(x)
            else:
                self.right = TreeNode(x)
        return

    # array to bst
    def insert_arr(self, ar : []):
        if len(ar) == 0: return

        for n in ar:
            self.insert(n)




################## DRIVER
def main():
    print ("[mst] binary tree doodle")

    head = TreeNode()    

    #  inserting values as the example shows: [4,2,7,1,3,6,9]
	#     4
	#    / \
	#   2   7
	#  / \  / \
	# 1   3 6  9
    arr = [4,2,7,1,3,6,9]
    head.insert_arr(arr)
    head.print_inorder()    


if __name__ == ("__main__"):
    main()
