class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD=(10**9)+7
        adj=[[]for _ in range(n)]
        for u,v,time in roads:
            adj[u].append((time,v))
            adj[v].append((time,u))

        dist=[float('inf')]*n
        dist[0]=0
        res=[0]*n
        res[0]=1
        ab=[(0,0)]
        while ab:
            time,node=heapq.heappop(ab)
            for newTime,newNode in adj[node]:
                if time+newTime<dist[newNode]:
                    dist[newNode]=time+newTime
                    heapq.heappush(ab,(dist[newNode],newNode))
                    res[newNode]=res[node]
                elif time+newTime==dist[newNode]:
                    res[newNode]=(res[newNode]+res[node])%MOD
        return int(res[n-1]%MOD)

        