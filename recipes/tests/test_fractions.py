from unittest import TestCase

from recipes.templatetags.fractions import to_frac

test_cases = {4: (
                ((0.1), 0),
                ((0.2), (0,1,4)),
                ((0.3), (0,1,3)),
                ((0.4), (0,1,3)),
                ((0.5), (0,1,2)),
                ((0.6), (0,2,3)),
                ((0.7), (0,2,3)),
                ((0.8), (0,3,4)),
                ((0.9), 1),
                ((1.0), 1),
              )}

class TestFractions(TestCase):
    def test_to_frac(self):
        for maxdenom, x_and_expected in test_cases.iteritems():
            for x, expected in x_and_expected:
                result = to_frac(x, maxdenom)
                self.assertEquals(result, expected)
