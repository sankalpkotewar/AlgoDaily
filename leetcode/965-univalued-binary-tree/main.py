# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: recursive dfs

    Time    O(n)
    Space   O(h)
    20 ms, faster than 58.34%
"""


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.hs = set()
        self.dfs(root)
        return len(self.hs) == 1

    def dfs(self, node):
        if node == None:
            return
        self.hs.add(node.val)
        self.dfs(node.left)
        self.dfs(node.right)


"""
    2nd approach: iterative dfs

    Time    O(n)
    Space   O(h)
    20 ms, faster than 58.34%
"""


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        hs = set()
        stack = [root]
        while len(stack) > 0:
            pop = stack.pop()
            hs.add(pop.val)
            if pop.left != None:
                stack.append(pop.left)
            if pop.right != None:
                stack.append(pop.right)
        return len(hs) == 1


"""
    3rd approach: bfs

    Time    O(n)
    Space   O(h)
    20 ms, faster than 58.34%
"""


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        hs = set()
        q = [root]
        while len(q) > 0:
            head = q.pop(0)
            hs.add(head.val)
            if head.left != None:
                q.append(head.left)
            if head.right != None:
                q.append(head.right)
        return len(hs) == 1
