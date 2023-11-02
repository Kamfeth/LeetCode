class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for i, j in enumerate(nums):
      if j > 0:
        break

      if i > 0 and j == nums[i - 1]:
        continue

      leftIndex, rightIndex = i + 1, len(nums) - 1
      while leftIndex < rightIndex:
        threeSum = j + nums[leftIndex] + nums[rightIndex]
        if threeSum > 0:
          rightIndex -= 1
        elif threeSum < 0:
          leftIndex += 1
        else:
          result.append([j, nums[leftIndex], nums[rightIndex]])
          leftIndex += 1
          rightIndex -= 1
          while nums[leftIndex] == nums[leftIndex - 1] and leftIndex < rightIndex:
            leftIndex += 1
            
    return result
