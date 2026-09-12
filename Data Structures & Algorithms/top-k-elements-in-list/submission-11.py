class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l=[[] for i in range(len(nums)+1)]

        for i in nums:
            d[i]= d.get(i,0)+1

        for s,v in d.items():
            l[v].append(s)

        res=[]

        for i in range(len(l)-1,0,-1):
            for n in l[i]:
                res.append(n)
                if len(res)==k:
                    return res



        
        
        