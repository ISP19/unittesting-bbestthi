import math


class Fraction:
   """A fraction with a numerator and denominator and arithmetic operations.
   Fractions are always stored in proper form, without common factors in
   numerator and denominator, and denominator >= 0.
   Since Fractions are stored in proper form, each value has a
   unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
   internal representation.
   """

   def __init__(self, numerator, denominator=1):
   """Initialize a new fraction with the given numerator
   and denominator (default 1).
   """

      if not isinstance(numerator, int):
         raise TypeError
      elif not isinstance(denominator, int):
         raise TypeError

      elif denominator < 0 and numerator > 0:
         numerator = int(numerator*-1)
         denominator = int(denominator*-1)

      elif denominator < 0 and numerator < 0:
         numerator = abs(numerator)
         denominator = abs(denominator)

      elif denominator == 0:
         if numerator == 0:
            self.denominator = 0
            self.numerator = 0
         elif numerator < 0:
            self.numerator = -1
            self.denominator = 0
         elif numerator > 0:
            self.numerator = 1
            self.denominator = 0
      else:
         gcd = math.gcd(numerator, denominator)
         self.numerator = int(numerator/gcd)
         self.denominator = int(denominator/gcd)

   def __add__(self, frac):
      numerator = (self.numerator*frac.denominator)+(self.denominator*frac.numerator)
      denominator = (self.denominator*frac.denominator)
      return Fraction(numerator,denominator)



    # TODO write __mul__ and __str__.  Verify __eq__ works with your code.
    # Optional have fun and overload other operators such as 
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)

   def __eq__(self, frac):
   """Two fractions are equal if they have the same value.
   Fractions are stored in proper form so the internal representation
   is unique (3/6 is same as 1/2).
   """
      self.numerator = self.numerator/gcd
      self.denominator = self.denominator/gcd
      return self.numerator/self.denominator == frac.numerator/frac.denominator

   def __mul__(self,frac):
   """Return the sum of two fractions as a new fraction.
      Use the standard formula  a/b * c/d = (a*c)/(b*d)
   """
      numerator = self.numerator*frac.numerator
      denominator = self.denominator*frac.denominator
      return Fraction(numerator,denominator)

   def __sub__(self,frac):
   """Return the sum of two fractions as a new fraction.
      Use the standard formula  a/b - c/d = (ad-cb)/(bd)
   """
      numerator = (self.numerator*frac.denominator)-(frac.numerator*self.denominator)
      denominator = self.numerator/frac.denominator
      return Fraction(numerator,denominator)

   def __div__(self):
   """Return the sum of two fractions as a new fraction.
      Use the standard formula  (a/b) / (c/d) = (a*d)/(b*c)
   """
      numerator = self.numerator*frac.denominator
      denominator = self.denominator*frac.numerator
      return Fraction(numerator,denominator)


   def __str__(self):
      if self.denominator==1:
         return self.numerator
      else:
         return self.numerator/self.denominator

