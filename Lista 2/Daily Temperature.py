class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
      while stack and t > stack[-1][0]:
        temperatures, indexes = stack.pop()
        result[indexes] = i - indexes
      stack.append((t, i))
    return result
