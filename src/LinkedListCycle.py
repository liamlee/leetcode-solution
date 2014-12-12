#Given a linked list, determine if it has a cycle in it.

#Follow up:
#Can you solve it without using extra space?

import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class List:
	def createTailToHeadCycleList(self,n):
		head = ListNode(0)
		preNode = head
		for i in range(n):
			curNode = ListNode(i)
			preNode.next = curNode
			preNode = curNode
		#make cycle
		preNode.next = head

		return head

	def createCycleList(self,n):
		head = ListNode(0)
		preNode = head
		for i in range(n):
			curNode = ListNode(i)
			preNode.next = curNode
			preNode = curNode
		#make cycle
		curNode = head
		for i in range(random.randint(0,n)):
			curNode = curNode.next
		#print("index:",i)
		preNode.next = curNode

		return head

	def createNonCycleList(self,n):
		head = ListNode(0)
		preNode = head
		for i in range(n):
			curNode = ListNode(i)
			preNode.next = curNode
			preNode = curNode

		return head


class Solution:
    # @param head, a ListNode
    # @return a boolean
    # this function can only recognize one case: tail-to-head cycle
    def hasCycle_tail_to_head(self, head):
    	curNode = head
    	if curNode is None:
    		return False
    	while curNode.next is not None:
    		if curNode.next == head:
    			return True
    		curNode = curNode.next
    	return False

    #WTF  AttributeError: 'NoneType' object has no attribute 'next'
    def hasCycle(self, head):
    	if head is None or head.next is None or head.next.next is None:
    		return False
    	slow = head.next
    	fast = head.next.next
    	while slow is not None and fast is not None:
    		if fast == slow:
    			return True
    		if fast.next is None:
    			return False
    		fast = fast.next.next
    		slow = slow.next
    	return False

if __name__ == '__main__':
	s = Solution()
	cycleList = List()
	print(s.hasCycle(cycleList.createTailToHeadCycleList(100)))
	print(s.hasCycle(cycleList.createNonCycleList(100)))
	print(s.hasCycle(cycleList.createCycleList(1000000)))