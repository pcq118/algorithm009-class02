#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (75.43%)
# Likes:    1141
# Dislikes: 0
# Total Accepted:    144.5K
# Total Submissions: 190.9K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例：
# 
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
# 
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #递归
        res = []
        def recursion(left, right, n, s): 
            if left == n and right == n:
                res.append(s)
                return 
            if left < n:
                recursion(left + 1, right, n,s +'(' )
            if left > right:
                recursion(left, right + 1, n, s + ')')
        recursion(0, 0, n, "")
        return res
# @lc code=end

