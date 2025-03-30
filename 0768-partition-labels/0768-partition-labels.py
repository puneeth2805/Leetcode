class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res=[]
        end=0
        k=0
        dic=dict(zip(s,count()))
        for i,c in enumerate(s):
            end=max(end,dic[c])
            k+=1
            if i==end:
                res.append(k)
                k=0
        return res

        