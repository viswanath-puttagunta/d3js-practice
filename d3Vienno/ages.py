#!/bin/python
import numpy as np


ages = map(int, list(np.random.normal(40,30,200)))
ages = map(abs, ages)
f = open("ages.csv", 'w')
f.write('"name","age"\n')

for i in ages:
	f.write('"Max",' + str(i) + '\n')
f.close()

