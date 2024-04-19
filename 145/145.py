# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[3,2,1]
#
#
#  示例 2：
#
#
# 输入：root = []
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：root = [1]
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  树中节点的数目在范围 [0, 100] 内
#  -100 <= Node.val <= 100
#
#
#
#
#  进阶：递归算法很简单，你可以通过迭代算法完成吗？
#
#  Related Topics 栈 树 深度优先搜索 二叉树 👍 1171 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional,List
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            res.append(root.val)


        helper(root)
        return res

        # Test cases

test_cases = [
    # Empty tree
    # (None, []),

    # Single node
    # (TreeNode(1), [1]),
    #
    # # Two-level tree
    # (TreeNode(1, None, TreeNode(2)), [1, 2]),
    # (TreeNode(1, TreeNode(2), None), [2, 1]),

    # Three-level tree
    (TreeNode(1, None, TreeNode(2, TreeNode(3), None)), [1, 3, 2]),
    (TreeNode(1, TreeNode(2, None, TreeNode(3)), None), [2, 3, 1]),

    # Balanced tree
    (TreeNode(4, TreeNode(2, None, TreeNode(3)), TreeNode(6, None, TreeNode(7))), [2, 3, 4, 6, 7]),

    # Unbalanced tree
    (TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3, None, TreeNode(5))), [4, 2, 1, 5, 3]),
]

for root, expected_result in test_cases:
    actual_result = Solution().inorderTraversal(root)
    print(f"Input: {root}")
    print(f"Expected: {expected_result}")
    print(f"Actual:   {actual_result}")
    print("-" * 20)