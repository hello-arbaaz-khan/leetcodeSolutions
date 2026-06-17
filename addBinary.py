# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
    
        # Dono strings ke pointers end se start karo
        i = len(a) - 1
        j = len(b) - 1
    
        while i >= 0 or j >= 0 or carry:
            # Current digit lo (agar string khatam ho gayi to 0 lo)
            digitA = int(a[i]) if i >= 0 else 0
            digitB = int(b[j]) if j >= 0 else 0
    
            # Teen cheezein add karo: digitA + digitB + carry
            total = digitA + digitB + carry
    
            # Jo digit result mein jayegi
            result = str(total % 2) + result
    
            # Carry calculate karo
            carry = total // 2
    
            i -= 1
            j -= 1
    
        return result

a = "110"
b = "11"
sul = Solution()
print(sul.addBinary(a,b))