class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        d1={}
        d2={}
        for i in s:
            if i not in d1.keys():
                d1[i]=s.count(i)
                
        for j in t:
            if j not in d2.keys():
                d2[j]=t.count(j)

        if d1==d2:
            return True

        else:
            return False
        