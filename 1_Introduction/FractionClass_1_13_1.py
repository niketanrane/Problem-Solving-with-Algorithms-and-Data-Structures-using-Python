__author__ = 'niketanrane'

def gcd(a, b):
    while a%b != 0:
        olda = a
        oldb = b

        a = oldb
        b = olda % oldb

    return b

class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print("%d / %d" %(self.num, self.den))

    def __str__(self):
        #This is needed to support print() function on this object
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        gcdNum = gcd(num, den)
        num //= gcdNum     #Double slashes are for integer division, single slash is flosting division
        den //= gcdNum
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        gcdNum = gcd(num, den)
        num //= gcdNum     #Double slashes are for integer division, single slash is flosting division
        den //= gcdNum
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den*other.den
        gcdNum = gcd(num, den)
        num //= gcdNum
        den //= gcdNum
        return Fraction(num, den)

    def __truediv__(self, other):
        #truediv performs normal division. floordiv performs integer division.
        num = self.num * other.den
        den = self.den * other.num
        gcdNum = gcd(num, den)
        num //= gcdNum
        den //= gcdNum
        return Fraction(num, den)

    def __eq__(self, other):
        # By default, eq will check for shallow copy(True only if adresses are same and not for values. So we are overriding the eq method.
        return self.num * other.den == self.den * other.num



mf = Fraction(-1,2)
mf.show()
print(mf.__str__()) #Defining str method means a way to show how to print. as print() uses str to convert object first to string and then print
print(mf)
f1 = Fraction(1,2)
f2 = Fraction(1,2)
print("Add:", f1+f2)
print("Equal:", f1==f2)
print("Sub ", f1-f2)
print("Mul ", f1*f2)
print("div ", f1/f2)