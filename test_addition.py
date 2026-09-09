import addition
import math

assert addition.add(5, 10) == 15
assert addition.add(0, 0) == 0
assert addition.add(-5, 5) == 0
assert addition.add(-3, -7) == -10
assert addition.add(2.5, 3.5) == 6.0
assert addition.add(1e10, 1e10) == 2e10
assert addition.add(1, -1) == 0
assert addition.add(100, 200) == 300
assert math.isclose(addition.add(0.1, 0.2), 0.3)