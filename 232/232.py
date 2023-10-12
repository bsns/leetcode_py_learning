# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
#
#  实现 MyQueue 类：
#
#
#  void push(int x) 将元素 x 推到队列的末尾
#  int pop() 从队列的开头移除并返回元素
#  int peek() 返回队列开头的元素
#  boolean empty() 如果队列为空，返回 true ；否则，返回 false
#
#
#  说明：
#
#
#  你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法
# 的。
#  你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
#
#
#
#
#  示例 1：
#
#
# 输入：
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# 输出：
# [null, null, null, 1, 1, false]
#
# 解释：
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
#
#
#
#
#
#
#
#  提示：
#
#
#  1 <= x <= 9
#  最多调用 100 次 push、pop、peek 和 empty
#  假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）
#
#
#
#
#  进阶：
#
#
#  你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。
#
#
#  Related Topics 栈 设计 队列 👍 1001 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MyQueue:

    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def push(self, x: int) -> None:
            self.stack_a.append(x)
            # while(self.stack_a):
            #     self.stack_b.append(self.stack_a.pop())

    def pop(self) -> int:
        if (self.stack_b):
            tmp = self.stack_b.pop()
        else:
            while (self.stack_a):
                self.stack_b.append(self.stack_a.pop())
            tmp = self.stack_b.pop()
        return tmp

    def peek(self) -> int:
        if (self.stack_b):
            return self.stack_b[-1]
        else:
            while (self.stack_a):
                self.stack_b.append(self.stack_a.pop())
        return self.stack_b[-1]

    def empty(self) -> bool:
        return len(self.stack_b) == 0 and len(self.stack_a) ==0



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()

# 测试用例: ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# 期望结果: [null, null, null, 1, 1, false]


# obj.push(1)
# obj.push(2)
# param_3 = obj.peek()
# param_2 = obj.pop()
# param_4 = obj.empty()
#
# print(param_3)
# print(param_2)
# print(param_4)



# 测试用例:["MyQueue","push","push","push","push","pop","push","pop","pop","pop","pop"]
# 			[[],[1],[2],[3],[4],[],[5],[],[],[],[]]
# 	测试结果:[null,null,null,null,null,1,null,5,2,3,4]
# 	期望结果:[null,null,null,null,null,1,null,2,3,4,5]
# obj.push(1)
# obj.push(2)
# obj.push(3)
# obj.push(4)
# print(obj.pop())
# print(obj.push(5))
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())



# 测试用例:["MyQueue","push","push","peek","push","peek"]
# 			[[],[1],[2],[],[3],[]]
# 	测试结果:[null,null,null,1,null,3]
# 	期望结果:[null,null,null,1,null,1]
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.push(3))
print(obj.peek())


