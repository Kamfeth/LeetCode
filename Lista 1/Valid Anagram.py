class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    counterOfSCharacters = {}
    counterOfTCharacters = {}

    for i in range(len(s)):
      counterOfSCharacters[s[i]] = 1 + counterOfSCharacters.get(s[i], 0)
      counterOfTCharacters[t[i]] = 1 + counterOfTCharacters.get(t[i], 0)
    return counterOfSCharacters == counterOfTCharacters
