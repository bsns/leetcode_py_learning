# 给定一个二叉树 root ，返回其最大深度。
#
#  二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
#
#
#
#  示例 1：
#
#
#
#
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
#
#
#  示例 2：
#
#
# 输入：root = [1,null,2]
# 输出：2
#
#
#
#
#  提示：
#
#
#  树中节点的数量在 [0, 10⁴] 区间内。
#  -100 <= Node.val <= 100
#
#
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1715 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        self.res = 0
        self.max_value = 0
        def helper(root):
            if not root:
                return

            self.res += 1
            self.max_value = max(self.res,self.max_value)

            helper(root.left)
            helper(root.right)

            self.res -=1

        helper(root)
        return self.max_value

Solution_sample = Solution()
a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c

c.left = d
c.right = e

# root = [3,9,20,null,null,15,7]
# 期望结果:3

res = Solution_sample.maxDepth(a)
print(res)



