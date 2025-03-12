class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left=[]
        count=0
        right=[]
        for num in nums:
            if num<pivot:
                left.append(num)
            elif num==pivot:
                count+=1
            else:
                right.append(num)
        return left+[pivot]*count+right

        
        