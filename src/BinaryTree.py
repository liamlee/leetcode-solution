# -*- coding: utf-8 -*-

class TreeNode:
	def __ini__(self,x):
		self.val = x
		self.left = None
		self.right = None

class BinaryTree():

	def buildTree(self,nodeList):
		if nodeList is None:
			return None
		bTree = []
		
		#元素节点化
		for item in nodeList:
			if item == '#':
				bTree.append(None)
				continue
			bTree.append(TreeNode(item))

		#建立二叉树
		i = 0
		n = len(nodeList)
		pos = 1
		while i < n and pos < n:
			if bTree[i] is not None:
				bTree[i].left = bTree[pos]
				pos += 1
				if pos < n :
					bTree[i].right = bTree[pos]
					pos += 1
			i += 1

		return bTree[0]
