class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
       covered = set()

       for start, end in ranges:
            for number in range(start, end + 1):
                covered.add(number)

       for number in range(left, right + 1):
            if number not in covered:
                return False

       return True

        
        