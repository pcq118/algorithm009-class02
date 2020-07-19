#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#
# https://leetcode-cn.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (39.33%)
# Likes:    231
# Dislikes: 0
# Total Accepted:    46.3K
# Total Submissions: 116.9K
# Testcase Example:  '"aba"'
#
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
# 
# 示例 1:
# 
# 
# 输入: "aba"
# 输出: True
# 
# 
# 示例 2:
# 
# 
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
# 
# 
# 注意:
# 
# 
# 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
# 
# 
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while i<=j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                x=s[i:j]
                y=s[i+1:j+1]
                return True if x[::-1]==x or y[::-1]==y else False
        return True
# @lc code=end

