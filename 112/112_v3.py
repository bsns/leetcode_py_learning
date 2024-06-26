# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和
#  targetSum 。如果存在，返回 true ；否则，返回 false 。
#
#  叶子节点 是指没有子节点的节点。
#
#
#
#  示例 1：
#
#
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# 输出：true
# 解释：等于目标和的根节点到叶节点路径如上图所示。
#
#
#  示例 2：
#
#
# 输入：root = [1,2,3], targetSum = 5
# 输出：false
# 解释：树中存在两条根节点到叶子节点的路径：
# (1 --> 2): 和为 3
# (1 --> 3): 和为 4
# 不存在 sum = 5 的根节点到叶子节点的路径。
#
#  示例 3：
#
#
# 输入：root = [], targetSum = 0
# 输出：false
# 解释：由于树是空的，所以不存在根节点到叶子节点的路径。
#
#
#
#
#  提示：
#
#
#  树中节点的数目在范围 [0, 5000] 内
#  -1000 <= Node.val <= 1000
#  -1000 <= targetSum <= 1000
#
#
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1350 👎 0

from typing import Optional
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, currentSum):
            # 如果节点为空，返回 False
            if not node:
                return False

            # 更新当前路径和
            currentSum += node.val

            # 如果当前节点是叶子节点，检查路径和是否等于目标和
            if not node.left and not node.right:
                return currentSum == targetSum

            # 递归检查左右子树
            return dfs(node.left, currentSum) or dfs(node.right, currentSum)

        # 从根节点开始调用内部函数，初始路径和为 0
        return dfs(root, 0)

        return helper(root, targetSum - root.val)