# 给你一棵二叉树的根节点，返回该树的 直径 。
#
#  二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
#
#  两节点之间路径的 长度 由它们之间边数表示。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,2,3,4,5]
# 输出：3
# 解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
#
#
#  示例 2：
#
#
# 输入：root = [1,2]
# 输出：1
#
#
#
#
#  提示：
#
#
#  树中节点数目在范围 [1, 10⁴] 内
#  -100 <= Node.val <= 100
#
#
#  Related Topics 树 深度优先搜索 二叉树 👍 1419 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) :

        self.res = 0
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)

            self.res = max(self.res, l+r+1)

            return max(l,r)+1

        dfs(root)
        return self.res -1


Solution_sample = Solution()
# a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(3)
# d = TreeNode(4)
# e = TreeNode(5)
#
# a.left = b
# a.right = c
#
# b.left = d
# b.right = e



a = TreeNode(1)
b = TreeNode(2)


a.left = b
# 期望结果:1


res = Solution_sample.diameterOfBinaryTree(a)
print(res)
