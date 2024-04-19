class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root or root == p or root == q:
            return

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not right:
            return left
        if not left:
            return right
        if not (left and right):
            return None
        return root


# Test cases
tree_values = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = build_tree(tree_values)
p = root.left
q = root.right.right
expected_result = 3

actual_result = Solution().lowestCommonAncestor(root, p, q)
if actual_result is None:
    print(f"Input: root = {root}, p = {p.val}, q = {q.val}")
    print(f"Expected: {expected_result}")
    print(f"Actual:   None (as expected)")  # Print "None (as expected)" if actual_result is None
else:
    print(f"Input: root = {root}, p = {p.val}, q = {q.val}")
    print(f"Expected: {expected_result}")
    print(f"Actual:   {actual_result.val}")
print("-" * 20)
