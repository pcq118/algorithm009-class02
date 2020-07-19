#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (23.60%)
# Likes:    415
# Dislikes: 0
# Total Accepted:    53K
# Total Submissions: 222.5K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 
# 示例 1:
# 
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
# 
# 示例 2:
# 
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# 
#

# @lc code=start

from functools import lru_cache
class Solution:
    @lru_cache(None)
    def numDecodings(self, s: str) -> int:
        #找重复性
        #f(n)= f(n-1)+ f(n-2)
        cnt = 0
        if len(s) == 0: return 1
        if s[0] != '0':
            cnt += self.numDecodings(s[1:])
        if 10 <= int(s[0:2]) <= 26:
            cnt += self.numDecodings(s[2:])
        return cnt

        
# @lc code=end

