#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (45.12%)
# Likes:    237
# Dislikes: 0
# Total Accepted:    86.6K
# Total Submissions: 189K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 
# 
# 
# 示例：
# 
# s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
# 
# 
# 
# 
# 提示：你可以假定该字符串只包含小写字母。
# 
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for c in s:
            if s.find(c) == s.rfind(c):
                return s.find(c)
        return -1
# @lc code=end

