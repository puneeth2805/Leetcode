class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canChoose(limit:int)->bool:
            count,i,n=0,0,len(nums)
            while i < n:
                if nums[i]<=limit:
                    count+=1
                    i+=2
                else:
                    i+=1
            return count>=k
        left,right=min(nums),max(nums)
        while left<right:
            mid=(left+right)//2
            if canChoose(mid):
                right=mid
            else:
                left=mid+1
        return left
        