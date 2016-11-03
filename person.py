from decimal import Decimal


class person:
    def __init__(self):
        self._fee = None
    @property
    def fee(self):
        return self._fee
    @fee.setter
    def fee(self,value,value2):
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value
    fee='001'

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, 2)
print v1 + v2