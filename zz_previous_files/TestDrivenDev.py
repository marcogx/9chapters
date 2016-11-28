import unittest
import datetime


class FooTests(unittest.TestCase):
	def testMatches(self):
		p = DatePattern(2004, 9, 28)
		d = datetime.date(2004, 9, 28)
		self.failUnless(p.matches(d))

	def testMatchesFalse(self):
		p = DatePattern(2004, 9, 30)
		d = datetime.date(2004, 9, 28)
		self.failIf(p.matches(d))

	def testMatchesYearAsWildCard(self):
		p = DatePattern(0, 4, 10)
		d = datetime.date(2015, 4, 10)
		self.failUnless(p.matches(d))

	def testMatchesWeekday(self):
		p = DatePattern(0, 0, 0, 2)  # 2 is Wednesday
		d = datetime.date(2004, 9, 29)
		self.failUnless(p.matches(d))

	def testMatchesYearAndMonthAsWildCards(self):
		p = DatePattern(0, 0, 1)
		d = datetime.date(2004, 10, 1)
		self.failUnless(p.matches(d))


class DatePattern:
	def __init__(self, year, month, day, weekday=0):
		self.year = year
		self.month = month
		self.day = day
		self.weekday = weekday

	def matches(self, date):
		return (self.yearMatches(date) and
		        self.monthMatches(date) and
		        self.dayMatches(date) and
		        self.weekdayMatches(date))

	def yearMatches(self, date):
		if not self.year: return True
		return self.year == date.year

	def monthMatches(self, date):
		if not self.month: return True
		return self.month == date.month

	def dayMatches(self, date):
		if not self.day: return True
		return self.day == date.day

	def weekdayMatches(self, date):
		if not self.weekday: return True
		return self.weekday == date.weekday()


def main():
	unittest.main()


if __name__ == '__main__':
	main()
