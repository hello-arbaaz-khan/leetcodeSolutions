# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Empty box

        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for chr in s:
            if chr in "({[":
                stack.append(chr)
            else:
                if not stack:
                    return False
                if stack[-1] == pairs[chr]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
            
s = "(){}[]"
sulation = Solution()
print(sulation.isValid(s))