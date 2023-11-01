class Solution:
  def isPalindrome(self, s: str) -> bool:
    leftIndex, rightIndex = 0, len(s) - 1
    while leftIndex < rightIndex:
      while leftIndex < rightIndex and not self.isAlphanum(s[leftIndex]):
        leftIndex += 1
      while leftIndex < rightIndex and not self.isAlphanum(s[rightIndex]):
        rightIndex -= 1
      if s[leftIndex].lower() != s[rightIndex].lower():
        return False
      leftIndex += 1
      rightIndex -= 1
    return True

  def isAlphanum(self, c):
    return ord("A") <= ord(c) <= ord("Z") or ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9")
