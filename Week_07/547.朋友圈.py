#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#
# https://leetcode-cn.com/problems/friend-circles/description/
#
# algorithms
# Medium (56.69%)
# Likes:    268
# Dislikes: 0
# Total Accepted:    50.1K
# Total Submissions: 87.5K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C
# 的朋友。所谓的朋友圈，是指所有朋友的集合。
# 
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j
# 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
# 
# 示例 1:
# 
# 
# 输入: 
# [[1,1,0],
# ⁠[1,1,0],
# ⁠[0,0,1]]
# 输出: 2 
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。
# 
# 
# 示例 2:
# 
# 
# 输入: 
# [[1,1,0],
# ⁠[1,1,1],
# ⁠[0,1,1]]
# 输出: 1
# 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
# 
# 
# 注意：
# 
# 
# N 在[1,200]的范围内。
# 对于所有学生，有M[i][i] = 1。
# 如果有M[i][j] = 1，则有M[j][i] = 1。
# 
# 
#

# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        f = {}
        s = {}
        count = len(M)

        def find(x):
            f.setdefault(x, x)
            # 路径压缩
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            nonlocal count
            x_father, y_father = find(x), find(y)
            if x_father == y_father: return
            # 将小树的根节点连接到大树的根节点
            if s.setdefault(x_father, 1) < s.setdefault(y_father, 1):
                f[x_father] = y_father
                s[y_father] += s[x_father]
            else:
                f[y_father] = x_father
                s[x_father] += s[y_father]
            count -= 1

        for i in range(len(M)):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1:
                    union(i, j)
        return count

# @lc code=end

