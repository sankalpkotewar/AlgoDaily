# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: iterative dfs
    - declare a result array
    - when we traverse down, put the val into the result if the depth > len(array)

    Time    O(n)
    Space   O(h)
    24 ms, faster than 74.45%
"""


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        stack = []
        stack.append((root, 1))
        while len(stack) > 0:
            node, depth = stack.pop()
            if depth > len(res):
                res.append(node.val)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return res


"""
    1st approach: bfs
    - declare a result array
    - when we traverse down, put the val into the result if the depth > len(array)

    Time    O(n)
    Space   O(h)
    16 ms, faster than 99.24%
    15may2019
"""


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        q = []
        q.append((root, 1))
        while len(q) > 0:
            node, depth = q.pop(0)
            if depth > len(res):
                res.append(node.val)
            if node.right:
                q.append((node.right, depth + 1))
            if node.left:
                q.append((node.left, depth + 1))
        return res
