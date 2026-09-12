class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        l = []
        while len(l) < k:
            x = max(d.values())
            for y in list(d.keys()):
                if d[y] == x and len(l) < k:
                    l.append(y)
                    del d[y]

        return l
        
        