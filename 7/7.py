class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        s = str(x)
        res = ''

        for i in range(len(s)):
            tmp = s[i]
            res = tmp + res

        res = flag * (int(res))
        if res > (2 ** 31 - 1) or res < -(2 ** 31):
            res = 0
        return res


def main():
    solution_instance = Solution()

    # Test Case 1
    # x1 = 123
    # result1 = solution_instance.reverse(x1)
    # print(f"Original Number: {x1}")
    # print(f"Result: {result1}")
    # print()
    #
    # # Test Case 2
    # x2 = -123
    # result2 = solution_instance.reverse(x2)
    # print(f"Original Number: {x2}")
    # print(f"Result: {result2}")
    # print()

    # Test Case 3
    x3 = 2147483651
    result3 = solution_instance.reverse(x3)
    print(f"Original Number: {x3}")
    print(f"Result: {result3}")
    print()

    # Test Case 4
    x4 = 0
    result4 = solution_instance.reverse(x4)
    print(f"Original Number: {x4}")
    print(f"Result: {result4}")
    print()


if __name__ == "__main__":
    main()
