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
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1268 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        def helper(node, target, now):
            if not node:
                return False
            now = now + node.val
            if node.left is None and node.right is None:
                return now == target

            else:
                return helper(node.left, target, now) or helper(node.right, target, now)

        res = helper(root, targetSum, 0)
        return res






Solution_sample = Solution()




def generate_tree(vals):
    if len(vals) == 0:
        return None
    que = [] # 定义队列
    fill_left = True # 由于无法通过是否为 None 来判断该节点的左儿子是否可以填充，用一个记号判断是否需要填充左节点
    for val in vals:
        node = TreeNode(val) if val is not None else None # 非空值返回节点类，否则返回 None
        if len(que)==0:
            root = node # 队列为空的话，用 root 记录根结点，用来返回
            que.append(node)
        elif fill_left:
            que[0].left = node
            fill_left = False # 填充过左儿子后，改变记号状态
            if node: # 非 None 值才进入队列
                que.append(node)
        else:
            que[0].right = node
            if node:
                que.append(node)
            que.pop(0) # 填充完右儿子，弹出节点
            fill_left = True #
    return root



#
# root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22

# test_tree = [5,4,8,11,None,13,4,7,2,None,None,None,1]
# targetSum = 22

# test_tree = [1,2,3]
# targetSum = 5
# # 期望结果:false


test_tree = []
targetSum = 0
# # 期望结果:false

a = generate_tree(test_tree)

res = Solution_sample.hasPathSum(a,targetSum)
print(res)




