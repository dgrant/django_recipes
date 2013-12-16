from django import template

register = template.Library()

def _to_frac(x, maxdenom=10):
    """
    Convert x to a common fraction.

    Chooses the closest fraction to x with denominator <= maxdenom.
    If x is closest to an integer, return that integer; otherwise,
    return an (integer, numerator, denominator) tuple.
    """

    assert x >= 0, "_to_frac only works on positive numbers."

    intpart = int(x)
    x -= intpart

    bestfrac = 0,1
    mindiff = x

    for denom in range(1,maxdenom+1):
        # for each denominator, there are two numerators to consider:
        # the one below x and the one above x
        for num in (int(x*denom), int(x*denom+1)):
            diff = abs(float(num)/denom - x)

            # compare using '<' rather than '<=' to ensure that the
            # fraction with the smallest denominator is preferred
            if diff < mindiff:
                bestfrac = num, denom
                mindiff = diff

    if bestfrac[0] == 0:
        return intpart
    elif mindiff >= 1-x:
        return intpart+1
    else:
        return intpart, bestfrac[0], bestfrac[1]

@register.filter
def html_fraction(number, maxdenom=10):
    """
    Convert a float to a common fraction (or an integer if it is closer).

    If the output is a fraction, the fraction part is wrapped in a span
    with class "fraction" to enable styling of fractions.
    """

    number = float(number)
    frac = _to_frac(abs(number), maxdenom)

    if type(frac) == int:
        string = str(frac)
    else:
        intpart, numerator, denominator = frac
        if intpart == 0:
            string = '<span class="fraction"><sup>%i</sup>/<sub>%i</sub></span>' % frac[1:]
        else:
            string = '%i<span class="fraction"><sup>%i</sup>/<sub>%i</sub></span>' % frac

    if number < 0:
        return '-'+string
    else:
        return string

@register.filter
def text_fraction(number, maxdenom=10):
    """Convert a float to a common fraction (or integer if it is closer)."""

    number = float(number)
    frac = _to_frac(abs(number), maxdenom)

    if type(frac) == int:
        string = str(frac)
    else:
        intpart, numerator, denominator = frac
        if intpart == 0:
            string = '%i/%i' % frac[1:]
        else:
            string = '%i %i/%i' % frac

    if number < 0:
        return '-'+string
    else:
        return string
