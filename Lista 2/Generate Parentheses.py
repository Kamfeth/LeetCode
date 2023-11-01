class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    stack = []
    result = []

    def calculateResult(openBracket, closedBracket):
      if openBracket == closedBracket == n:
        result.append("".join(stack))
        return

      if openBracket < n:
        stack.append("(")
        calculateResult(openBracket + 1, closedBracket)
        stack.pop()
      if closedBracket < openBracket:
        stack.append(")")
        calculateResult(openBracket, closedBracket + 1)
        stack.pop()

    calculateResult(0, 0)
    return result
