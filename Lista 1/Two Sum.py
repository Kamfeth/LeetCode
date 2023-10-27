class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    mapOfIndices = {}

    for i, j in enumerate(nums):
      difference = target - j
      if difference in mapOfIndices:
        return [mapOfIndices[difference], i]
      mapOfIndices[j] = i
