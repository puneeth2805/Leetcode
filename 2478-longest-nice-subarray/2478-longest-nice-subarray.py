class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        a=0
        maxLen=0
        i=0
        for j in range(len(nums)):
            while (a&nums[j])!=0:
                a^=nums[i]
                i+=1
            a|=nums[j]
            maxLen=max(maxLen,j-i+1)
        return maxLen

        