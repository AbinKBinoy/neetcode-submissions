class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns=""
        for i in s:
            if i.isalnum():
                ns=ns+i.lower()

        return ns == ns[::-1]
        