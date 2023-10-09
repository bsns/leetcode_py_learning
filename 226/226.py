# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
#
#
#
#  示例 1：
#
#
#
#
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]
#
#
#  示例 2：
#
#
#
#
# 输入：root = [2,1,3]
# 输出：[2,3,1]
#
#
#  示例 3：
#
#
# 输入：root = []
# 输出：[]
#
#
#
#
#  提示：
#
#
#  树中节点数目范围在 [0, 100] 内
#  -100 <= Node.val <= 100
#
#
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1704 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        def dfs(root):
            if not root:
                return None

            dfs(root.left)
            dfs(root.right)
            root.left, root.right = root.right ,root.left

            return root
        dfs(root)

        return root

Solution_sample = Solution()



# a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(3)
# a.left=b
# a.right=c



def construct_binary_tree(nums: []) -> TreeNode:
    if not nums:
        return None
    # 用于存放构建好的节点
    root = TreeNode(-1)
    Tree = []
    # 将数组元素全部转化为树节点
    for i in range(len(nums)):
        if nums[i]!= -1:
            node = TreeNode(nums[i])
        else:
            node = None
        Tree.append(node)
        if i == 0:
            root = node
    # 直接判断2*i+2<len(Tree)会漏掉2*i+1=len(Tree)-1的情况
    for i in range(len(Tree)):
        if Tree[i] and 2 * i + 1 < len(Tree):
            Tree[i].left = Tree[2 * i + 1]
            if 2 * i + 2 < len(Tree):
                Tree[i].right = Tree[2 * i + 2]
    return root
#
# test_tree = [4, 2, 7, 1, 3, 6, 9]
# a = construct_binary_tree(test_tree)


# [4,2,7,1,3,6,9]
# 测试结果:[4,7,2,9,6,1,3]
# 	期望结果:[4,7,2,9,6,3,1]

test_tree = [3,None,1,2]
a = construct_binary_tree(test_tree)

# 测试用例:[3,null,1,2]
# 	测试结果:[3,1,null,2]
# 	期望结果:[3,1,null,null,2]


res = Solution_sample.invertTree(a)
print(res)


def print_tree_level(root):
    if root is None:
        return

    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

print_tree_level(res)
