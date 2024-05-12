# 解题思路
# 用二维数组的python解法
#
# 代码
# python3
#

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # s1 = "PAYPALISHIRING"

        if numRows == 1: return s
        row_set = ["" for i in range(numRows)]
        cnt = 0
        res = ""

        flag = 1
        current_idx = 0
        while (cnt < len(s)):
            # print(cnt,s[cnt],current_idx)
            # print(row_set)
            # current_idx = cnt % (numRows * 2 - 2) #cnt%numRows
            if (flag == 1):
                row_set[current_idx] += s[cnt]
                current_idx = current_idx + 1
            else:

                row_set[current_idx] += s[cnt]
                current_idx = current_idx - 1
            if ((current_idx == numRows) and flag == 1) or (flag == -1 and current_idx == -1):
                # flag =-flag
                if (flag == 1):
                    current_idx = current_idx - 1 - 1
                else:
                    current_idx = current_idx + 1 + 1
                flag = -flag

            cnt += 1

        for i in row_set:
            res += i
        return res

def main():
    solution_instance = Solution()

    # Test Case 1
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    result1 = solution_instance.convert(s1, numRows1)
    print(f"Original String: {s1}")
    print(f"Result: {result1}")
    print()
    # 期望结果: "PAHNAPLSIIGYIR"
    # # Test Case 2
    # s2 = "PAYPALISHIRING"
    # numRows2 = 4
    # result2 = solution_instance.convert(s2, numRows2)
    # print(f"Original String: {s2}")
    # print(f"Result: {result2}")
    # print()
    #
    # # Add more test cases as needed...

if __name__ == "__main__":
    main()