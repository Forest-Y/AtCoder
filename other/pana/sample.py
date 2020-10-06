from math import sqrt
from decimal import *

a, b, c = map(int, input().split())
"""
print(sqrt(a), sqrt(b))
print(Decimal(sqrt(a)), sqrt(b))
"""

print("Yes" if Decimal(a).sqrt() + Decimal(b).sqrt() < Decimal(c).sqrt() else "No")