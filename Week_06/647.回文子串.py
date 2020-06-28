#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#
# https://leetcode-cn.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (61.69%)
# Likes:    269
# Dislikes: 0
# Total Accepted:    30.3K
# Total Submissions: 49.1K
# Testcase Example:  '"abc"'
#
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
# 
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
# 
# 示例 1:
# 
# 
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".
# 
# 
# 示例 2:
# 
# 
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 注意:
# 
# 
# 输入的字符串长度不会超过1000。
# 
# 
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += 1
            left, right = i - 1, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1 
                right += 1 
            left, right  = i - 1, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1 
                right += 1 
        return res
              
        
# @lc code=end

