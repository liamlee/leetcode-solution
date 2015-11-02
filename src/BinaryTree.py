# -*- coding: utf-8 -*-

class TreeNode:
	def __init__(self,x):
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

	def printTree(self,root):
		if root is None:
			print (None)
		to_travl = [root]

		while to_travl:
			cur_node = to_travl.pop()
			if cur_node is None:
				print("#")
				continue
			print(cur_node.val)
			to_travl.insert(0,cur_node.left)
			to_travl.insert(0,cur_node.right)

if __name__ == '__main__':
	list1 = ["3","9","20","#","#","15","7"]
	list2 = ["1","2","3","#","#","4","#","#","5"]
	list3 = ['1','2','3','4','5']
	bt = BinaryTree()
	print(bt.printTree(bt.buildTree(list1)))
	print(bt.printTree(bt.buildTree(list2)))
	print(bt.printTree(bt.buildTree(list3)))



