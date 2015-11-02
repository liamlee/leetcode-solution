# -*- coding: utf-8 -*-
#Puzzle
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.


OJ's Binary Tree Serialization:
The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

Here's an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
Subscribe to see which companies asked this question
"""

#Analysis



#Solution code
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#from BinaryTreeLevelOrderTraversal import BTree,TreeNode
from BinaryTree import BinaryTree

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        zigzag_level_order = []
        to_travl = [root]
        travl_flag = 'left'

        while to_travl :
          cur_travl = to_travl
          to_travl = []
          zigzag_level_item = []
          while cur_travl :
            cur_node = cur_travl.pop()
            zigzag_level_item.append(cur_node.val)
            if travl_flag == 'left' :
              if cur_node.left :
                to_travl.append(cur_node.left)
              if cur_node.right :
                to_travl.append(cur_node.right)
              travl_flag = 'right'
            else :
              if cur_node.right :
                to_travl.append(cur_node.right)
              if cur_node.left :
                to_travl.append(cur_node.left)
              travl_flag = 'left'
          #print zigzag_level_item
          zigzag_level_order.append(zigzag_level_item)

        return zigzag_level_order


if __name__ == '__main__':
  list1 = ["3","9","20","#","#","15","7"]
  list2 = ["1","2","3","#","#","4","#","#","5"]

  BT = BinaryTree()
  s = Solution()

  print s.zigzagLevelOrder(BT.buildTree(list1))
  print s.zigzagLevelOrder(BT.buildTree(list2))
  #print s.zigzagLevelOrder(BT.buildTree(list3))



