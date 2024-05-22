
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import defaultdict
        window = defaultdict(int)
        need = defaultdict(int)

        for i in p:
            need[i] += 1

        start = 0
        left, right = 0, 0
        flag = 0
        res = []
        while (right < len(s)):
            c = s[right]
            right += 1

            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    flag += 1

            if right - left >= len(p):

                if flag == len(need):
                    res.append(left)

                d = s[left]
                left += 1
                if d in need:
                    if need[d] == window[d]:
                        flag -= 1
                    window[d] -= 1

        return res


Solution_demo = Solution()
s ="cbaebabacd"
p = "abc"
res = Solution_demo.findAnagrams(s,p)
print(res)