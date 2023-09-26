# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
#
#
#
#  示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
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
#  -1000 <= Node.val <= 1000
#
#
#  Related Topics 树 广度优先搜索 二叉树 👍 1810 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root) :

        queue = []
        if not root:
            return queue
        queue.append(root)

        res = []
        while ( len(queue) > 0):
            tmp_queue = []
            tmp_res = [cur.val for cur in queue]
            res.append(tmp_res)

            for cur in queue:
                if(cur.left):
                    tmp_queue.append(cur.left)
                if(cur.right):
                    tmp_queue.append(cur.right)
            queue = tmp_queue
        return res


Solution_sample = Solution()

# a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(3)
#
# a.left = b
# a.right = c

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e

#         3
#    9       20
# null null 15 7

# 测试用例:[3,9,20,null,null,15,7]
# 	测试结果:[[3],[9],[20],[15],[7]]
# 	期望结果:[[3],[9,20],[15,7]]

res = Solution_sample.levelOrder(a)
print(res)
