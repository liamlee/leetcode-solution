#Given an array of integers, every element appears twice except for one. Find that single one.

#Note:
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
	# @param A, a list of integer
    # @return an integer
	
	# every time using "in" will cost time ,so time out !!!
    #def singleNumber(self, A):
	#    while A:
	#		item = A.pop()
	#		if item in A:
	#			continue
	#		else:
	#			return item

	# using dict,so using extra memory!!!	
	def singleNumberByDict(self,A):
		d = {}
		for item in A:
			if str(item) in d:
				d[str(item)] += 1
			else:
				d[str(item)] = 1

		print(d)

		for k,v in d.items():
			if v == 1:
				return int(k)



if __name__ == '__main__':
	s = Solution()
	list1 = [1,2,3,4,5,1,2,3,4]
	list2 = [1]
	

	print(s.singleNumberByDict(list1))
	print(s.singleNumberByDict(list2))
							            
