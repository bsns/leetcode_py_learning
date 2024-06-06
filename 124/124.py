# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定
# 经过根节点。
#
#  路径和 是路径中各节点值的总和。
#
#  给你一个二叉树的根节点 root ，返回其 最大路径和 。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
#
#  示例 2：
#
#
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
#
#
#
#
#  提示：
#
#
#  树中节点数目范围是 [1, 3 * 10⁴]
#  -1000 <= Node.val <= 1000
#
#
#  Related Topics 树 深度优先搜索 动态规划 二叉树 👍 2229 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = float('-inf')

        def helper(node):
            if not node:
                return 0

            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)

            cur_max = left + right + node.val
            self.max_val = max(self.max_val, cur_max)

            return max(left, right) + node.val

        helper(root)

        return self.max_val


Solution_demo = Solution()

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
# 测试用例:[1,2,3]
# 期望结果:6
res = Solution_demo.maxPathSum(a)
print(res)