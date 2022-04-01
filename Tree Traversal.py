# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 23:13:40 2022

@author: tom97
"""

## Inorder Traversal


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        if root == None:
            return output
        return self.inorderTraversal_helper(root,output)
        
        
    def inorderTraversal_helper(self,start,traversal):
        if start:
            self.inorderTraversal_helper(start.left,traversal)
            traversal.append(start.val)
            self.inorderTraversal_helper(start.right,traversal)
            
        return traversal



## Post order Travesal

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = [] 
        if(root==None):
            return output
        return self.postorderTraversal_helper(root,output)
        
    def postorderTraversal_helper(self,start,traversal):
         if start:
            
            self.postorderTraversal_helper(start.left, traversal)
            self.postorderTraversal_helper(start.right, traversal)
            traversal.append(start.val)
        
         return traversal




## Pre order Traversal


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = [] 
        if(root==None):
            return output
        return self.preorderTraversal_helper(root,output)
        
    def preorderTraversal_helper(self,start,traversal):
         if start:
            traversal.append(start.val)
            self.preorderTraversal_helper(start.left, traversal)
            self.preorderTraversal_helper(start.right, traversal)
            
        
         return traversal