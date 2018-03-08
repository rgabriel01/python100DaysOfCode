class YearUtilities:
    def __init__(self, year):
        self.year = year

    def is_leap_year(self):
        if (self._divisible_by(4) and
            self._divisible_by(100) and
            self._divisible_by(400) or
            self._divisible_by(4)):
            return True
        else:
            return False

    def _divisible_by(self, divisor):
        return (self.year % divisor) == 0

print(YearUtilities(1805).is_leap_year())
