class Solution:
  def maxArea(self, height: List[int]) -> int:
    leftIndex, rightIndex = 0, len(height) - 1
    result = 0

    while leftIndex < rightIndex:
      result = max(result, min(height[leftIndex], height[rightIndex]) * (rightIndex - leftIndex))
      if height[leftIndex] < height[rightIndex]:
        leftIndex += 1
      elif height[rightIndex] <= height[leftIndex]:
        rightIndex -= 1
            
    return result
