"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        def dfs(root, depth):
            if not root: return 
            if len(res) <= depth:
                res.append([])
            res[depth].append(root.val)
            for ch in root.children:
                dfs(ch, depth+1)
        
        dfs(root, 0)
        return res
