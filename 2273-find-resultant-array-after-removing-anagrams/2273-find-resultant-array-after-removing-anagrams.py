class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        result = []
        
        prev_signature = None
        for word in words:
            current_signature = tuple(sorted(word))
            if current_signature != prev_signature:
                result.append(word)
                prev_signature = current_signature
            
        return result 