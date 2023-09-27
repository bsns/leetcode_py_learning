# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
#
#
#  示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[20,9],[15,7]]
#
#
#  示例 2：
#
#
# 输入：root = [1]
# 输出：[[1]]
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
#  树中节点数目在范围 [0, 2000] 内
#  -100 <= Node.val <= 100
#
#
#  Related Topics 树 广度优先搜索 二叉树 👍 817 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        stack = []
        res = []
        if not root:
            return res
        stack.append(root)

        flag = 0
        while(len(stack) > 0 ):

            tmp_stack = []
            tmp_res = [tmp.val for tmp in stack]
            if(flag%2 == 1):
                tmp_res.reverse()

            res.append(tmp_res)

            for tmp in stack:
                if tmp.left:
                    tmp_stack.append(tmp.left)
                if tmp.right:
                    tmp_stack.append(tmp.right)

            stack = tmp_stack

            flag += 1
        return res



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

# [3,9,20,null,null,15,7]

res = Solution_sample.zigzagLevelOrder(a)
print(res)
