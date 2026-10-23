class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        kel = celsius + 273.15
        fer = celsius*1.80 + 32.00

        return [kel,fer]