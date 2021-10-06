#!/usr/bin/python
# -*- coding: utf-8 -*-
# deterministic method
import time

inf_limit = 0
sup_limit = 500
# time counter
start = time.time()
for i in range(inf_limit,sup_limit+1):
    sum = 0
    for digit in [int(d) for d in str(i)]:
        sum = sum + digit*digit
    if i == sum:
        print(i)
elapsedTime = time.time() - start
print("Elapsed time: "+str(round(elapsedTime,4)))