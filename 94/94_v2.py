class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional,List
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)

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