"""
Conversion functions.
"""
import operator

from forml.io.dsl.schema import series, kind as kindmod


class Cast(series.Expression):
    """Explicitly cast value as given kind.
    """
    value: series.Element = property(operator.itemgetter(0))
    kind: kindmod.Any = property(operator.itemgetter(1))

    def __new__(cls, value: series.Element, kind: kindmod.Any):
        return super().__new__(cls, value, kind)
