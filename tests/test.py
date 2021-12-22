from pylib_general import properties
varname = properties.Property()
varname.add("something", 1122)
print(varname.something)
print(varname.get("something"))
varname.remove("something")
print(e)
try:
	print(varname.something)
except:
	print()
from pylib_general import math
print(math.recpow(2))
print(math.pow(2, 2))
print(math.pi)
print(math.sig(5))
print(math.factorial(5))
print(math.incr(1))
print(math.decr(1))
print(math.mod(1, 1))
