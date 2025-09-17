class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = set()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while r>l:
                tmp = nums[i] + nums[l] + nums[r]
                if (tmp == 0):
                    result.add((nums[i],nums[l],nums[r]))
                if (tmp > 0):
                    r-=1
                else:
                    l+=1

        listResult = list(result)
        return listResult 