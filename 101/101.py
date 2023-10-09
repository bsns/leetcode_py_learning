# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#
#
#  示例 2：
#
#
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#
#
#
#
#  提示：
#
#
#  树中节点数目在范围 [1, 1000] 内
#  -100 <= Node.val <= 100
#
#
#
#
#  进阶：你可以运用递归和迭代两种方法解决这个问题吗？
#
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 2563 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root):

        def dfs(left,right):
            if not (left or right):
                return  True

            if not(left and right):
                return False
            if (left.val != right.val):
                return False
            return dfs(left.left ,right.right) and dfs(left.right,right.left)

        return dfs(root.left,root.right)


Solution_sample = Solution()
# a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(2)
# d = TreeNode(3)
# e = TreeNode(4)
# f = TreeNode(4)
# g = TreeNode(3)
# #
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.left = f
# c.right = g



a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

#
a.left = b
a.right = c
# 期望结果:false


res = Solution_sample.isSymmetric(a)
print(res)
