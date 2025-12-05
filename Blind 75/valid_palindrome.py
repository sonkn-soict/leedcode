class Solution():
    def isPalidrome(self, s: str) -> bool:
        newstr = ""
        for c in str:
            if c.isalnum(): newstr += c.lower()
        return newstr == newstr[::-1]
    def isPalidrome_v2(self, s: str) -> bool: 
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.check_numeric(s[l]): l += 1
            while l < r and not self.check_numeric(s[r]): r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
    def check_numeric(self, c) -> bool:
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))
    
str = "Was it a car or a cat I saw?"
sol = Solution()
res = sol.isPalidrome(str)
print(res)

res_v2 = sol.isPalidrome_v2(str)
print(res_v2)
