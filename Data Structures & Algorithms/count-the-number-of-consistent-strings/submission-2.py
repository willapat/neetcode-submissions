class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        output = 0

        letters = set(allowed)
        for i in range(0, len(words)):
            if all(char in allowed for char in words[i]):
                output += 1
            
        return output