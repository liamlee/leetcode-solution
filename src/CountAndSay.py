#----------------------------------------------------------
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#312211 13112221 1113213211

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#----------------------------------------------------------

# Note: The sequence of integers will be represented as a string.

#Solution: directory will be a nice chioce ?  不行，如count_err()方法中，不能得到正确结果

class Solution:
    # @return a string
    def countAndSay(self, n):
    	string = '1'
    	for i in range(n-1):
    		string = self.myCountAndSay(string)
    	return string

    #扫描sequence，对当前字符进行计数，相邻字符不同时，前一个字符及其计数并如string中，重新开始新字符的计数
    def myCountAndSay(self,sequence):
    	s = ''
    	pre_ch = sequence[0]
    	count = 0
    	for cur_ch in sequence:
    		if cur_ch == pre_ch:
    			count += 1
    		else:
    			s += str(count) + pre_ch
    			count = 1
    		pre_ch = cur_ch
    	s += str(count) + cur_ch
    	return s

    def count_err(self,sequence):
    	words = {}
    	pre_ch = ''
    	for cur_ch in sequence:
    		print(pre_ch,cur_ch)
    		if cur_ch == pre_ch:
    			words[cur_ch] = words[cur_ch] + 1   
    		else:
    			words[cur_ch] = 1    #会将已存在的key重置
    		pre_ch = cur_ch
    	print(words)
    	return words

if __name__ == '__main__':
	s = Solution()
	print(s.countAndSay(6))