from math import sqrt


class Fraction:
	def __init__(self, top, bottom):
		self.num = top
		self.den = bottom


	def __add__(self, newFraction):
		tempNum = (self.num * newFraction.den) + (self.den * newFraction.num)
		tempDen = self.den * newFraction.den
		com = getCD(tempNum, tempDen)
		return Fraction(tempNum // com, tempDen // com)


	def __sub__(self, newFraction):
		tempNum = (self.num * newFraction.den) - (self.den * newFraction.num)
		tempDen = self.den * newFraction.den
		com = getCD(tempNum, tempDen)
		return Fraction(tempNum // com, tempDen // com)

	def __mul__(self, newFraction):
		tempNum = self.num * newFraction.num
		tempDen = self.den * newFraction.den
		com = getCD(tempNum, tempDen)
		return Fraction(tempNum // com, tempDen // com)

	def __truediv__(self, newFraction):
		tempNum = self.num * newFraction.den
		tempDen = self.den * newFraction.num
		com = getCD(tempNum, tempDen)
		return Fraction(tempNum / com, tempDen / com)
		#return Fraction(tempNum , tempDen)

	def __floordiv__(self, newFraction):
		tempNum = self.num * newFraction.den
		tempDen = self.den * newFraction.num
		com = getCD(tempNum, tempDen)
		return Fraction(tempNum // com, tempDen // com)
		#return Fraction(tempNum , tempDen)

	def __mod__(self, newFraction):
		pass
		'''tempNum = (self.num * newFraction.den) + (self.den * newFraction.num)
		tempDen = self.den * newFraction.den
		com = getCD(tempNum, tempDen)
		return Fraction(tempNum // com, tempDen // com)'''


	def __and__(self, newFraction):
		tempNum = (self.num * newFraction.den) & (self.den * newFraction.num)
		tempDen = self.den * newFraction.den
		com = getCD(tempNum, tempDen)
		return Fraction(tempNum // com, tempDen // com)


	def __or__(self, newFraction):
		tempNum = (self.num * newFraction.den) | (self.den * newFraction.num)
		tempDen = self.den * newFraction.den
		com = getCD(tempNum, tempDen)
		return Fraction(tempNum // com, tempDen // com)

	def __xor__(self, newFraction):
		tempNum = (self.num * newFraction.den) ^ (self.den * newFraction.num)
		tempDen = self.den * newFraction.den
		com = getCD(tempNum, tempDen)
		return Fraction(tempNum // com, tempDen // com)


	def __str__(self):
		return str(self.num) + "/" + str(self.den)



	def __eq__(self, newFraction):
		tempSelf = self.num * newFraction.den
		tempNew = newFraction.num * self.den
		return tempSelf == tempNew


	def __lt__(self, newFraction):
		tempSelf = self.num * newFraction.den
		tempNew = newFraction.num * self.den
		return tempSelf < tempNew


	def __le__(self, newFraction):
		tempSelf = self.num * newFraction.den
		tempNew = newFraction.num * self.den
		return tempSelf <= tempNew



	def __ne__(self, newFraction):
		tempSelf = self.num * newFraction.den
		tempNew = newFraction.num * self.den
		return tempSelf != tempNew


	def __gt__(self, newFraction):
		tempSelf = self.num * newFraction.den
		tempNew = newFraction.num * self.den
		return tempSelf > tempNew


	def __ge__(self, newFraction):
		tempSelf = self.num * newFraction.den
		tempNew = newFraction.num * self.den
		return tempSelf >= tempNew





def getCD(num, den):
	while num%den != 0:
		tempNum = num

		num = den
		den = tempNum% den
	return den



f1 = Fraction(2, 6)

f2 = Fraction(3, 4)

res = f1 + f2


print("working f1:", f1)
print("working f2:", f2)
print("working sum:", f1 + f2)
print("working sub:", f2 - f1)
print("working mult:", f1 * f2)
print("working div:", f1 / f2)
print("working div:", f1 // f2)
print("working eq:", f1 == f2)
print("working lt:", f1 < f2)
print("working le:", f1 <= f2)
print("working gt:", f1 > f2)
print("working ge:", f1 >= f2)
print("working ne:", f1 != f2)
