class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    leftIndex, rightIndex = 0, len(numbers) - 1

    while leftIndex < rightIndex:
      curSum = numbers[leftIndex] + numbers[rightIndex]

      if curSum > target:
        rightIndex -= 1
      elif curSum < target:
        leftIndex += 1
      else:
        return [leftIndex + 1, rightIndex + 1]
