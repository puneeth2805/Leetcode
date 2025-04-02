class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        maxVal=0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    currVal=(nums[i]-nums[j])*nums[k]
                    if currVal>maxVal:
                        maxVal=currVal
        if maxVal>0:
            return maxVal
        else:
            return 0

        