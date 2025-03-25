class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x=sorted([(i[0],i[2])for i in rectangles],key=lambda x:x[0])
        y=sorted([(i[1],i[3])for i in rectangles],key=lambda x:x[0])
        def valid_cut(intervals):
            c=0
            ce=intervals[0][1]
            for start,end in intervals[1:]:
                if ce<=start:
                    c+=1
                ce=max(ce,end)
                if c==2:
                    return True
            return False
        return valid_cut(x) or valid_cut(y)