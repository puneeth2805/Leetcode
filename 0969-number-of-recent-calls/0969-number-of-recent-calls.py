class RecentCounter:

    def __init__(self):
        self.records=[]
        self.st=0
        
        

    def ping(self, t: int) -> int:
        self.records.append(t)
        while self.records[self.st]<t-3000:
            self.st+=1
        return len(self.records)-self.st

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)