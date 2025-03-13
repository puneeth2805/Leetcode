class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n=len(nums)
        m=len(queries)
        zero_arr=[0]*(n+1)
        a,count=0,0
        for i in range(n):
            while a<nums[i]-zero_arr[i]:
                if count>=m:
                    return -1
                left,right,val=queries[count]
                if right<i:
                    count+=1
                    continue
                zero_arr[max(left,i)]+=val
                zero_arr[right+1]-=val
                count+=1
            a+=zero_arr[i]
        return count
            
            



        