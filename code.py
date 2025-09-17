class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue
            l = i+1
            r = len(nums)-1
            while r>l:
                tmp = nums[i] + nums[l] + nums[r]
                if (tmp == 0):
                    result.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l + 1]: l += 1
                    while l < r and nums[r] == nums[r - 1]: r -= 1
                    
                if (tmp > 0):
                    r-=1
                else:
                    l+=1
        return result 