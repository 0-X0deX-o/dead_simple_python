from decimal import Decimal
from fractions import Fraction

third_fraction = Fraction(1, 3)
third_fixed = Decimal("0.333")
third_float = 1 / 3

print(third_fraction)
print(third_fixed)
print(third_float)

third_float = float(third_fraction)
print(third_float)

third_float = float(third_fixed)
print(third_float)

two_thirds_fraction = Fraction(2, 3)
two_thirds_fixed = Decimal("0.666")
print(third_fixed + two_thirds_fixed) 
print(third_fraction + two_thirds_fraction) 
