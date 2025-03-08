class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        size=n*n
        count=[0]*(size+1)
         
        for i in range(n):
            for j in range(n):
                count[grid[i][j]]+=1
        a,b=-1,-1
        for ele in range(1,size+1):
            if count[ele]==2:
                a=ele
            elif count[ele]==0:
                b=ele
        return [a,b]
        
        

        