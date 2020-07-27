''' constructing binary tree from postorder and inorder traversal

    Problem Statement:
    Given inorder and postorder traversal of a tree, construct the binary tree.

    Note:
    You may assume that duplicates do not exist in the tree.

    For example, given

    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    Return the following binary tree:

     3
    / \
   9  20
     /  \
    15   7

Algorithm Inorder(tree):
    1. Traverse the left subtree, i.e., call Inorder(left-subtree)
    2. Visit the root.
    3. Traverse the right subtree, i.e., call Inorder(right-subtree)
Uses of Inorder:
    In case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order. 
    To get nodes of BST in non-increasing order, a variation of Inorder traversal where Inorder traversal s reversed can be used.

Algorithm Postorder(tree)
   1. Traverse the left subtree, i.e., call Postorder(left-subtree)
   2. Traverse the right subtree, i.e., call Postorder(right-subtree)
   3. Visit the root.
Uses of Postorder:
    Postorder traversal is used to delete the tree. 
    Please see the question for deletion of tree for details. 
    Postorder traversal is also useful to get the postfix expression of an expression tree. 
    Please see http://en.wikipedia.org/wiki/Reverse_Polish_notation to for the usage of postfix expression.
'''
# Definition for a binary tree node.
# Input:
#   inorder -> list of integers
#   postorder -> list of integers
# Output:
#   TreeNode

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def buildTree(self, inorder, postorder):
        return TreeNode

    def display_inorder(self, root):
        if root:
            self.display_inorder(TreeNode(root).left)
            print(TreeNode(root).val)
            self.display_inorder(TreeNode(root).right)
    def display_postorder(self, root):
        if root:
            self.display_postorder(TreeNode(root).left)
            self.display_postorder(TreeNode(root).right)
            print(TreeNode(root).val)