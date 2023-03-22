'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "". 

'''
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
            for i in range (len(strs)):
                my_list = strs[0:1] 
            print(my_list)

s = Solution()
strs = ['hello', 'hi', 'how']
print(s.longestCommonPrefix(strs))