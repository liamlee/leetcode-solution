# -*- coding: utf-8 -*-
#Puzzle
'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
Subscribe to see which companies asked this question
'''

#Analysis
'''
直接扫描方式
len = 1 -> s.length
	if len < s.length / 2
		s1,s2,s3,...
		if len == 1
			所有子串直接如结果集
		else 
			if 所有子串都为回文
				所有子串放入结果集
  切割s,s1 = s[:len], s2 = s[len:]
  如果 所有子串都为回文，所有子串放入结果集
  否则 跳过
返回结果集

'''

#Solution code
class Solution(object):
	def is_palindrome(self,s):
		if s == s[::-1]:
			return True
		else :
			return False

	def partition(self, s):
		"""
		:type s: str
		:rtype: List[List[str]]
		"""
		if s == '' :
			return None

		possible_part_list = []

		str_len = len(s)
		if str_len == 1 :
			return [[s]]
		length = 1
		while length <= str_len :
			#partition way 1
			if length == 1 and str_len != 2:
				possible_part_list.append([i for i in s])
			elif length < str_len / 2 :
				start = 0
				end = start + length
				cur_part_list = []
				flag = 1
				while start < str_len :
					ss = s[start:end]
					cur_part_list.append(ss)
					if self.is_palindrome(ss):
						flag *= 1
					else :
						flag *= 0
						break
					start = end
					end += length
				if flag == 1 :
					possible_part_list.append(cur_part_list)
			else :
				pass

			#partition way 2
			if length == str_len :
				if self.is_palindrome(s) :
					possible_part_list.append([s])
					break
			s1 = s[:length]
			s2 = s[length:]
			if self.is_palindrome(s1) and self.is_palindrome(s2) :
				possible_part_list.append([s1,s2])
			length += 1

		return possible_part_list




if __name__ == '__main__':
	Solu = Solution()
	s = ''
	#print Solu.is_palindrome(s)
	print Solu.partition('abbab')
	#print Solu.partition('a')
	#print Solu.partition('aa')
	#print Solu.partition('ab')
	#print Solu.partition('aba')
	#print Solu.partition('abc')
	#print Solu.partition('aab')
	#print Solu.partition('aaaabb')
	#print Solu.partition('aabaaaaaaaaaaaaaaab')
	#print Solu.partition('aabaaweregaaaaaaaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaaaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabbaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabdsfaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabdfvaaabaaweregaaaaaadsfdfvasfaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabsfryhsaaaaarhgaabaabaaweregaaaaaaaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaaaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabbaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabdsfaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabdfvaaabaaweregaaaaaadsfdfvasfaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabryhsaaaaarhgaabaabaaweregaaaaaadsfdfvasfryhsaaaaarhgaabsfryhsaaaaarhgaab')



