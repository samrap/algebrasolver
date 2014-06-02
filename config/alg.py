from __future__ import division
from fractions import Fraction, gcd
import math

"""Algebra calculation module

This module takes user input from the algebra.py module and
processes calculations based on the function called by the user.
Functions in this module should never be called explicitly in
this script, aside from testing.

Besides testing, these functions are typically called from the
algebra.py module. The exception to this is complicated equations
that may require multiple functions to be completed.
"""

# ---------- GLOBAL CALCULATIONS ---------- #

def remove_zeros(iterable, replace=1):
    """Remove zeros from a list.

    This function is typically used to prevent a ZeroDivisionError when
    dividing by numbers in a list. By default the number replaced has
    the value of 1, unless the 'replace' parameter is specified.
    """

    for num in xrange(0, len(iterable)):
        if iterable[num] == 0:
            iterable[num] = replace
    return iterable

def check(x):
    """Return only the sign of an integer x if its value is 1. If its
    value is greater than 1, return the value.
    """

    if x == -1: return '-'
    if x == 1: return ''
    return x

def atod(a):
    """Attempt to convert the data type 'a' to digit d

    This function is used for converting a string to a digit when the exact type
    is unknown (i.e. integer or float). If the string cannot be converted, the
    function returns False. Otherwise, the digit is returned as a float if the
    decimal is greater than 0 or as an integer if the decimal is equal to 0.

    Due to the nature of the function, it can also be used to round off floating
    point numbers whose decimal is equal to 0 (i.e. 3.0 -> 3)
    """

    try:
        d = float(a)
    except:
        return False

    if d == int(d):
        # it is an integer
        return int(d)
    else:
        return d


# ---------- SPECIFIC CALCULATIONS ---------- #

def direct_variation(x, y):
    """Check if the values of y vary directly with the values of x.

    Find the constant of variation between the first two x/y values
    and check the remaining values against that constant. Print if
    y varies directly with x or not and if it does, include the
    constant of variaition (k).
    """

    # Check if any value in the x tuple is equal to 0.
    if any((n == 0 for n in x)):
        print "Zero division error. Type 'man dv' for more info."
        return False

    k = Fraction(y[0], x[0])

    if all([Fraction(x[1], x[0]) == k for x in zip(x, y)]):
        print "Y varies directly with x. k = %s" % (k)
    else:
        print "Y does not vary directly with x"

def find_slope(set_one, set_two):
    """Find the slope between two x,y coordinate sets using the
    equation y2 - y1 / x2 - x1 and return it in simplest form.
    """
    try:
        print Fraction(set_two[1] - set_one[1], set_two[0] - set_one[0])
    except ZeroDivisionError:
        print "Undefined"

def numtype(n):
    """Print the type of number entered.

    For example, the number 12 is a real, natural number, the number -2 is a
    real integer, etc.
    """

    ntype = type(n)
    if ntype == int:
        if n > 0:
            print "%s is a real, natural number" % (n)
            return
        if n >= 0:
            print "%s is a real, whole number" % (n)
            return
        if n < 0:
            print "%s is a real integer" % (n)
    elif ntype == float:
        print "%s is a real, rational number" % (n)
        return
    else:
        print "Error: %s is not a number" % (n)
        return

def check_arithmetic_sequence(sequence, n):
    """Check if the given data, sequence  is an arithmetic sequence.

    If sequence is not an arithmetic sequence, print that it is not and return
    False. If sequence is an arithmetic sequence, print the common difference
    as well as n, the nth term, if the flag was specified.

    A list of numbers is an arithmetic sequence if there is a common difference
    between each term and its preceding term. If any of the differences do not
    match, it is not a sequence.
    """

    i, j = 0, 1
    # Establish a common difference to check against for all terms
    diff = sequence[j] - sequence[i]
    while j < len(sequence):
        if sequence[j] - sequence[i] != diff:
            print "Not an arithmetic sequence"
            return False
        i += 1; j += 1
    else:
        print "The sequence is an arithmetic sequence. Common difference: %s"\
                                                                        % (diff)
    if n:
        print "Nthterm: %s" % (sequence[0] + (n - 1) * diff)

def check_geometric_sequence(sequence, n):
    """Check if the given data is a geometric sequence.

    If sequence is not a geometric sequence, print that it is not and return
    False. If sequence is a geometric sequence, print the common ratio as well
    as n, the nth term, if the flag was specified.

    A list of numbers is a geometric sequence if there is a common ratio
    between each term and its preceding term. If any of the ratios do not match,
    it is a not a sequence. 
    """

    # Prevent a 0 division error. sequence[n] must always be greater than 0
    if any((n == 0 for n in sequence)):
        print "Zero division error. Type 'man sq' for more info."
        return False

    i, j = 0, 1
    # Establish a ratio to check against for all terms
    ratio = sequence[j] / sequence[i]
    while j < len(sequence):
        if sequence[j] / sequence[i] != ratio:
            print "Not a geometric sequence"
            return False
        i += 1; j += 1
    else:
        # Convert ratio to integer if decimal is 0
        ratio = atod(ratio)
        print "The sequence is a geometric sequence. Common ratio: %s" % (ratio)

    if n:
        print "Nthterm: %s" % (sequence[0] * (ratio**(n - 1)))

def arithmetic_series(fterm, nterm, n):
    """Print and return the series of an arithmetic sequence.

    The series of an arithmetic sequence is the sum of every value in the
    sequence. In this function, a sequence is assumed. See /manuals/sr for more
    info.
    """

    ssum = atod(n / 2 * (fterm + nterm))
    print "Sum of the finite arithmetic series: %s" % ssum
    return ssum

def geometric_series(fterm, nterm, ratio):
    """Print and return the series of an geometric sequence.

    The series of an geometric sequence is the sum of every value in the
    sequence. In this function, a sequence is assumed. See /manuals/sr for more
    info.
    """

    # Find n, the number of elements in the series, round off decimal if needed
    n = atod(math.log10(nterm / fterm) / math.log10(ratio) + 1)
    # Use n to find the sum of the series
    ssum = atod((fterm * (1 - ratio**n)) / (1 - ratio))

    print "Sum of the geometric series: %s" % ssum
    return ssum


class Quadratic(object):

    def __init__(self, a, b, c):
        """Create a new instance of the quadratic object.

        Quadratic takes exactly three arguments: the a, b, and c values
        of a quadratic formula. This object contains many methods related
        to the quadratic equation and quadratic functions.
        """
        self.a = a
        self.b = b
        self.c = c

    def FindVertex(self, out=True):
        """Given the a, b, and c values of the quadratic function,
        calculate and print the vertex. Return h and k, as this
        function is sometimes called by other functions. If the 'out'
        parameter is False, return the values else print the vertex.
        """

        h = -self.b / (2 * self.a)  # -b / 2a
        k = ((self.a * h * h) + (self.b * h) + self.c)  # f(-b / 2a)

        if not out: return h, k
        print "Vertex: ({}{},{}{})".format('- '[h < 0], abs(h),
                                           ' -'[h < 0], abs(k))


    def VertexForm(self):
        """Convert the standard form of a quadratic to vertex form ie
        y = a(x - h)^2 + k.
        """

        vertex = self.FindVertex(False)
        h, k = vertex[0], vertex[1]

        print u"{}(x {} {})\u00b2 {} {}".format(check(self.a), '-+'[h < 0],
                                                abs(h), '+-'[k < 0], abs(k))

    # Complete the square given the 'b' term of a quadratic equation.
    def CompleteSquare(self): print (self.b / 2) ** 2

    def Discriminant(self, value=False):
        """Find the value of the discriminant and return or print its value.

        The discriminant is  b^2 - 4ac,  the value under the radical of the
        quadratic equation. This method can be used either as a return value or
        to print the discriminant and number of solutions to stdout, depending
        on the 'value' parameter.
        """

        d = self.b * self.b - 4 * self.a * self.c

        if value is True: return d

        if d > 0:
            print "The discriminant is %s. There are 2 solutions." % d
        elif d == 0:
            print "The discriminant is %s. There is 1 solution." % d
        else:
            print "There are no real solutions."

    def FactorizeQuadratic(self):
        """Factorize the quadratic expression ax^2 + bx + x over the real
        numbers and print the factorization. If it is not factorable,
        raise an error. If the sol parameter is True, include solutions
        to the x values.

        ----- Examples -----

        >>> factorize_quadratic(1, 4, 4)
        (x + 2)(x + 2)
        >>> factorize_quadratic(1, -4, 4)
        (x - 2)(x - 2)
        >>> factorize_quadratic(7, 19, -6)
        (7x - 2)(x + 3)
        """

        # Make life easier
        a, b, c = self.a, self.b, self.c

        # Find common factor, if any
        f = abs(gcd(gcd(a, b), c))
        a, b, c = a // f, b // f, c // f

        # Check if the discriminant is a perfect square.
        # If it is not, the equation is not factorable.
        discriminant = self.Discriminant(True)
        root = int(math.sqrt(abs(discriminant)))
        if root * root != discriminant:
            print "No real number factorization is possible"
            return False

        # The sorted function is strictly for visual purposes. It insures that
        # the factorization will be (x + 2)(x - 1) instead of (x - 1)(x + 2).
        r, s = sorted((Fraction(-b - root, 2 * a),
                       Fraction(-b + root, 2 * a)), key=abs)

        def factor(t):
            if t == 0: return "x"
            n, d = t.numerator, t.denominator
            return "({}x {} {})".format(check(d), '-+'[n < 0], abs(n))

        print "{}{}{}".format(check(f), factor(r), factor(s))
        return True


class Radical(object):

    def __init__(self, rad, root=2):
        self.rad = rad
        self.root = root

    def FindRoot(self): print self.rad ** (1 / self.root)


if __name__ == '__main__':
    #check_geometric_sequence((4,12,36), False)
    geometric_series(3, 3072, 2)
