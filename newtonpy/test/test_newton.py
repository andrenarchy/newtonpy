import unittest
from numpy import sin, cos, abs

from newtonpy.newton import newton


class NewtonTest(unittest.TestCase):
    def test_sin(self):
        assert(abs(newton(sin, cos, 0.5)) < 1e-8)

    def test_polynomial(self):
        print("test_sin")
