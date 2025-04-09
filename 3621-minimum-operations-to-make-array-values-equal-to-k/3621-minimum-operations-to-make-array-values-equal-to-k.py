class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums)<k:
            return -1
        s=set(nums)
        return len(s)-(min(nums)==k)
        