class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    setOfNumbers = set(nums)
    result = 0

    for n in setOfNumbers:
      if (n - 1) not in setOfNumbers:
        length = 1
        while (n + length) in setOfNumbers:
          length += 1
        result = max(length, result)
    return result
