class Solution:
  def trap(self, height: List[int]) -> int:
    if not height:
      return 0

    leftIndex, rightIndex = 0, len(height) - 1
    leftMax, rightMax = height[leftIndex], height[rightIndex]
    result = 0

    while leftIndex < rightIndex:
      if leftMax < rightMax:
        leftIndex += 1
        leftMax = max(leftMax, height[leftIndex])
        result += leftMax - height[leftIndex]
      else:
        rightIndex -= 1
        rightMax = max(rightMax, height[rightIndex])
        result += rightMax - height[rightIndex]
    return result
