class Solution:
    def isPalindrome(self, s: str) -> bool:
        numStr = ""
        for c in s:
            if c.isalnum():
                numStr += c.lower()
        return numStr == numStr[::-1]

# --- Add this part to test it in VS Coded ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    test_str = "A man, a plan, a canal: Panama"
    print(sol.isPalindrome(test_str))  # Expected output: True
    
    # Test case 2
    test_str_2 = "race a car"
    print(sol.isPalindrome(test_str_2))  # Expected output: False