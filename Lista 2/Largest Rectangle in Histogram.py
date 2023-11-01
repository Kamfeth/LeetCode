class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    areaOfLargestRectangleInHistogram = 0
    stack = []  # pair: (index, height)

    for i, h in enumerate(heights):
      temp = i
      while stack and stack[-1][1] > h:
        index, height = stack.pop()
        areaOfLargestRectangleInHistogram = max(areaOfLargestRectangleInHistogram, height * (i - index))
        temp = index
      stack.append((temp, h))

    for i, h in stack:
      areaOfLargestRectangleInHistogram = max(areaOfLargestRectangleInHistogram, h * (len(heights) - i))
    return areaOfLargestRectangleInHistogram
