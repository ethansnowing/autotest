#-*_coding:utf8-*-
# __author__ = ethan

import pylab
import math

x_values = []
y_values = []
num = 0.0

while num < math.pi*4:
    y_values.append(math.sin(num))
    x_values.append(num)
    num += 0.1

# now plot
pylab.plot(x_values, y_values, 'ro')
pylab.show()