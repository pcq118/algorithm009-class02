"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        list = []
        #根,左,右
        list.append(root.val)
        if root.children:
            for item in root.children:
                list += self.preorder(item)
        return list
