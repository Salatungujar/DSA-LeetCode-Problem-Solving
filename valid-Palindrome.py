class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Agar left wala character alphanumeric nahi hai, toh aage badho
            while left < right and not s[left].isalnum():
                left += 1
            
            # Agar right wala character alphanumeric nahi hai, toh peeche jao
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Case-insensitive comparison
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True
