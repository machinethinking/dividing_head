#!/usr/bin/env python
from math import sqrt
import sys


def gcd(a, b):
    """
    Return greatest common denominator of a and b

    >>> gcd(5, 10)
    5
    >>> gcd(5, 7)
    1
    """
    while 1:
        r = a % b
        if r == 0:
            break
        else:
            a, b = b, r
    return b


def factors(n):
    """
    Return a list of factors for n

    >>> factors(6)
    [1, 6, 2, 3]
    >>> factors(12)
    [1, 12, 2, 6, 3, 4]
    """
    fact = [1, n]
    check = 2
    rootn = sqrt(n)
    while check < rootn:
        if n % check == 0:
            fact.append(check)
            fact.append(n / check)
        check += 1
    if rootn == check:
        fact.append(check)
        fact.sort()
    return fact


def main(num_to_divide):
    """
    >>> main(13)
    index plate 39
    Complete turns: 3 plus 3 holes
    >>> main(21)
    index plate 21
    Complete turns: 1 plus 19 holes

    """

    # index plates for my dividing head
    plates = [15, 16, 17, 18, 19, 20, 21, 23, 27, 29, 31, 33, 37, 39,
              41, 43, 47, 49]
    # the ratio of the dividing head
    ratio = 40

    plate_dict = {}
    for i in plates:
        plate_dict[i] = factors(i)

    gcdi = gcd(ratio, num_to_divide)
    gcd_ratio = ratio / gcdi
    gcd_num_to_divide = num_to_divide / gcdi

    for k, v in sorted(plate_dict.items()):
        if gcd_num_to_divide in v:
            print "index plate %s" % k
            multiplier = k / gcd_num_to_divide
            turns = (gcd_ratio * multiplier) / (gcd_num_to_divide * multiplier)
            holes = (gcd_ratio * multiplier) % (gcd_num_to_divide * multiplier)
            print "Complete turns: %s plus %s holes" % (turns, holes)

if __name__ == "__main__":

    # run with unit tests
    # python -m doctest divide.py -v
    try:
        num_to_divide = int(sys.argv[1])
    except:
        print "usage: %s [number of divisions]" % sys.argv[0]
        sys.exit(0)

    main(num_to_divide)
