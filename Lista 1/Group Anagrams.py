class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for s in strs:
      counter = [0] * 26
      for c in s:
        counter[ord(c) - ord("a")] += 1
      anagrams[tuple(counter)].append(s)
    return anagrams.values()
