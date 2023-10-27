class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    counter = {}
    frequency = [[] for i in range(len(nums) + 1)]

    for n in nums:
      counter[n] = 1 + counter.get(n, 0)
    for n, c in counter.items():
      frequency[c].append(n)

    result = []
    for i in range(len(frequency) - 1, 0, -1):
      for n in frequency[i]:
        result.append(n)
        if len(result) == k:
          return result
