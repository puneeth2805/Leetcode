class Solution:
    def compress(self, chars: List[str]) -> int:
        res=0
        i=0
        while i<len(chars):
            char=chars[i]
            count=0
            while i<len(chars) and chars[i]==char:
                count+=1
                i+=1
            chars[res]=char
            res+=1
            if count>1:
                for c in str(count):
                    chars[res]=c
                    res+=1
        return res
        

        