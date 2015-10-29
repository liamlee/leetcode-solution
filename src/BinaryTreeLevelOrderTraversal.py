# -*- coding: utf-8 -*-

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BTree():
    #def __init__(self):
    #    self.root = None

    def buildTree(self,treeList):
        if treeList is None:
            return None
        bTree = []
        i = 0
        n = len(treeList)
        #元素节点化
        for item in treeList:
            if item == "#":
                bTree.append(None)
                continue
            bTree.append(TreeNode(item))

        #建立二叉树
        i = 0
        pos = 1
        while i < n and pos < n:
            if bTree[i] is not None:
                bTree[i].left = bTree[pos]
                pos = pos + 1
                if pos < n:
                    bTree[i].right = bTree[pos]
                    pos = pos + 1
            i = i + 1

        return bTree[0]

    def printTree(self,root):
        if root is None:
            print(None)
        to_travl = [root]

        while to_travl:
            cur_node = to_travl.pop()
            if cur_node is None:
                print("#")
                continue
            print(cur_node.val)
            to_travl.insert(0,cur_node.left)
            to_travl.insert(0,cur_node.right)


# v_1.0 time out
#仔细思考后，这个算法time out 是没道理的
#其实应该是错误，因为没有做列表清空，如23行注释，添上该语句，发现检测显示结果不对，
#原因是遍历顺序不正确
#如27、30、32行，这是把list当作stack用了，导致遍历顺序出错
#如v1.1，更正为queue，终于Accepted了。Bingo！
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder_err(self, root):
        level_Order = []
        level_item = []
        to_travl = [root]
        if root is None:
            return []
        while to_travl:
            cur_to_travl = to_travl
            to_travl = []
            #level_item = []
            while cur_to_travl:
                cur_node = cur_to_travl.pop()
                level_item.append(cur_node.val)
                if cur_node.left:
                    to_travl.append(cur_node.left)
                if cur_node.right:
                    to_travl.append(cur_node.right)
            level_Order.append(level_item)
        return level_Order

# v_1.1 accept
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        level_Order = []
        level_item = []
        to_travl = [root]
        if root is None:
            return []
        while to_travl:
            cur_to_travl = to_travl
            to_travl = []
            level_item = []
            while cur_to_travl:
                cur_node = cur_to_travl.pop()
                level_item.append(cur_node.val)
                if cur_node.left:
                    to_travl.insert(0,cur_node.left)
                if cur_node.right:
                    to_travl.insert(0,cur_node.right)
            level_Order.append(level_item)
        return level_Order


if __name__ == '__main__':
    list1 = ["3","9","20","#","#","15","7"]
    list2 = ["1","2","3","#","#","4","#","#","5"]
    bt = BTree()
    s = Solution()
    #print(bt.printTree(bt.buildTree(list2)))

    print(s.levelOrder(bt.buildTree(list1)))
    print(s.levelOrder(bt.buildTree(list2)))
