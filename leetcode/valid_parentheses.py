# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:

# Input: s = "()"
# Output: true


from operator import contains
import unicodedata


def valid_parens(parens_str):
    closeAndOpen = {")": "(", "}": "{", "]": "["}
    stack = []

    for parens in parens_str:
        if parens in closeAndOpen:
            # stack is not empty and last item in stack equals opening parens
            if stack and stack[-1] == closeAndOpen[parens]:
                stack.pop()
            else:
                return False
        else:
            stack.append(parens)
    # True if stack is empty        
    return True if not stack else False

print(valid_parens(")"))