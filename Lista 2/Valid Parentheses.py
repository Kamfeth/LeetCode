class Solution:
  def isValid(self, s: str) -> bool:
    parentheses = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
      if c not in parentheses:
        stack.append(c)
        continue
      if not stack or stack[-1] != parentheses[c]:
        return False
      stack.pop()

    return not stack
