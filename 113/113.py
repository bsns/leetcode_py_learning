# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
#
#  叶子节点 是指没有子节点的节点。
#
#
#
#
#
#
#
#  示例 1：
#
#
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
#
#
#  示例 2：
#
#
# 输入：root = [1,2,3], targetSum = 5
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：root = [1,2], targetSum = 0
# 输出：[]
#
#
#
#
#  提示：
#
#
#  树中节点总数在范围 [0, 5000] 内
#  -1000 <= Node.val <= 1000
#  -1000 <= targetSum <= 1000
#
#
#  Related Topics 树 深度优先搜索 回溯 二叉树 👍 1055 👎 0

from typing import  Optional,List
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(node,path,need,res):
            if  not node:
                return
            path.append(node.val)

            # if need < 0 or not node:
            #     return

            if (node.left is None and node.right is None and node.val == need):

                res.append(path[:])
                path.pop()
                return


            dfs(node.left,path,need - node.val ,res)
            dfs(node.right,path,need - node.val  ,res)

            path.pop()
            need+=node.val

        path = []
        res = []
        dfs(root,path,targetSum,res)

        return res


Solution_sample = Solution()

# a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(3)
# a.left = b
# a.right = c
# targetSum = 4



# [5,4,8,11,null,13,4,7,2,null,null,5,1]

# a = TreeNode(5)
# b = TreeNode(4)
# c = TreeNode(8)
# d = TreeNode(11)
#
# e = TreeNode(13)
# f = TreeNode(4)
# g = TreeNode(7)
# h = TreeNode(2)
#
# i = TreeNode(5)
# j = TreeNode(1)
#
# a.left = b
# a.right =c
# b.left =d
# d.left=g
# d.right=h
#
# c.left = e
# c.right = f
#
# f.left=i
# f.right=j
# targetSum = 22

# 测试结果:[[5,4,11,2],[5,4,8,4,5]]
# 	期望结果:[[5,4,11,2],[5,8,4,5]]


a = TreeNode(-2)
c = TreeNode(-3)

a.right =c
targetSum = -5
# 期望结果:[[-2,-3]]
res = Solution_sample.pathSum(a,targetSum)
print(res)