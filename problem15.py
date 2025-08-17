# There are 40 turns you need to make in each path from the top left
# to the bottom right.
# They can either be a 1 or a 0, but there must be an even number of
# 1s and 0s so 20 1s and 20 0s.
# This is just 40 choose 20 or 40!/(20!*20!)

import math as m
print ((m.factorial(40)/(m.factorial(20)**2)))
