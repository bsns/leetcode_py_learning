class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i,j = len(nums)-2 ,len(nums)-1
        while i>=0 and nums[i] >= nums[i+1] : i-=1
        if(i>=0):
            while j>i and nums[j]<=nums[i]:
                j-=1
            nums[i],nums[j] = nums[j],nums[i]
            tmp = nums[i+1:]
            tmp.sort()
            nums[i+1:] = tmp
        else:
            nums.sort()

        return nums

Solution_sample = Solution()
# res = Solution_sample.nextPermutation([3,2,1])

# res = Solution_sample.nextPermutation([1,3,2])
# res = Solution_sample.nextPermutation([2,3,1])


# res = Solution_sample.nextPermutation([5,4,7,5,3,2])
# res = Solution_sample.nextPermutation([4,2,0,2,3,2,0])
res = Solution_sample.nextPermutation([1,5,1])
print(res)