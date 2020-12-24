# Problem: a binary tree is said to be height-balanced if for each node in the tree, the difference in the height of
#          it's left and right subtrees is at most one. A perfect binary tree is height-balanced, as is a complete
#          binary tree. A height-balanced tree does not have to be perfect or complete.
#           Write a program that takes as input the root of a binary tree and checks whether the tree is height-balanced.

from collections import namedtuple

class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

# EPI Judge: is_tree_balanced.py
def is_balanced_binary_tree(tree):
    Tree_balance = namedtuple("Tree_balance", ("is_balanced","height"))
    
    def check_balance(tree):
        if not tree:
            return Tree_balance(True, -1) # (is_balanced?, height)

        balanceLeft = check_balance(tree.left)
        if not balanceLeft.is_balanced:
            return Tree_balance(False, 0)

        balanceRight = check_balance(tree.right)
        if not balanceRight.is_balanced or ( abs(balanceLeft.height-balanceRight.height) > 1):
            return Tree_balance(False, 0)

        curr_height = max(balanceLeft.height, balanceRight.height)

        return Tree_balance(True, curr_height + 1)

    return check_balance(tree).is_balanced

