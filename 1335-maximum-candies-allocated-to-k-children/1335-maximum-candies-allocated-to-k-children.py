class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left=1
        right=max(candies)
        res=0
        while left<=right:
            mid=(left+right)//2
            count=sum(pile//mid for pile in candies)
            if count>=k:
                res=mid
                left=mid+1
            else:
                right=mid-1
        return res

        