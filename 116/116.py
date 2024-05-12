# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
#
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#
#  填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
#  初始状态下，所有 next 指针都被设置为 NULL。
#
#
#
#  示例 1：
#
#
#
#
# 输入：root = [1,2,3,4,5,6,7]
# 输出：[1,#,2,3,#,4,5,6,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由
# next 指针连接，'#' 标志着每一层的结束。
#
#
#
#
#
#  示例 2:
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
#  树中节点的数量在
#  [0, 2¹² - 1] 范围内
#  -1000 <= node.val <= 1000
#
#
#
#
#  进阶：
#
#
#  你只能使用常量级额外空间。
#  使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
#
#
#  Related Topics 树 深度优先搜索 广度优先搜索 链表 二叉树 👍 1116 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    # 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
    # 本代码不保证正确性，仅供参考。如有疑惑，可以参照我写的 java 代码对比查看。

    # 主函数
    def connect(root: 'Node') -> 'Node':
        if root is None:
            return None

        # 三叉树遍历框架
        def traverse(node1: 'Node', node2: 'Node'):
            if node1 is None or node2 is None:
                return
            # 将传入的两个节点穿起来
            node1.next = node2

            # 连接相同父节点的两个子节点
            traverse(node1.left, node1.right)
            traverse(node2.left, node2.right)
            # 连接跨越父节点的两个子节点
            traverse(node1.right, node2.left)

        # 遍历「三叉树」，连接相邻节点
        traverse(root.left, root.right)
        return root





