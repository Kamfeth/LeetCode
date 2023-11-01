class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    for c in tokens:
      if c == "+":
        stack.append(stack.pop() + stack.pop())
      elif c == "-":
        firstValue, secondValue = stack.pop(), stack.pop()
        stack.append(secondValue - firstValue)
      elif c == "*":
        stack.append(stack.pop() * stack.pop())
      elif c == "/":
        firstValue, secondValue = stack.pop(), stack.pop()
        stack.append(int(float(secondValue) / firstValue))
      else:
        stack.append(int(c))
    return stack[0]
