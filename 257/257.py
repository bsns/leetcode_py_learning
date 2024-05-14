# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
#
#  叶子节点 是指没有子节点的节点。
#
#  示例 1：
#
#
# 输入：root = [1,2,3,null,5]
# 输出：["1->2->5","1->3"]
#
#
#  示例 2：
#
#
# 输入：root = [1]
# 输出：["1"]
#
#
#
#
#  提示：
#
#
#  树中节点的数目在范围 [1, 100] 内
#  -100 <= Node.val <= 100
#
#
#  Related Topics 树 深度优先搜索 字符串 回溯 二叉树 👍 1137 👎 0
import builtins
from typing import List
from typing import Optional
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def helper(cur, tmp, res):
            if not cur.left and not cur.right:  # 到达叶子节点
                tmp.append(cur.val)
                sPath = '->'.join(map(str, tmp))
                res.append(sPath)
                return
            tmp.append(cur.val)
            if cur.left:  # 左

                helper(cur.left, tmp, res)
                tmp.pop()  # 回溯
            if cur.right:  # 右

                helper(cur.right, tmp, res)
                tmp.pop()  # 回溯
            # tmp.pop()

        res = []
        tmp = []
        if not root:
            return res

        helper(root, tmp, res)
        return res



Solution_demo = Solution()
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.right = TreeNode(5)
# 期望结果:["1->2->5","1->3"]
res= Solution_demo.binaryTreePaths(a)
print(res)
