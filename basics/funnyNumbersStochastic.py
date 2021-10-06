#!/usr/bin/python
# -*- coding: utf-8 -*-
# stochastic method
import time
import random

inf_limit = 0
sup_limit = 500
# time counter
start = time.time()
# memory register
reg = []
for i in range(int((sup_limit-inf_limit)/2)):
    sum = 0
    random_value = random.randint(inf_limit,sup_limit)
    reg.append(random_value)
    if (random_value not in reg):
        for digit in [int(d) for d in str(random_value)]:
            sum = sum + digit*digit
        if random_value == sum:
            print(random_value)
elapsedTime = time.time() - start
print("Elapsed time: "+str(round(elapsedTime,4)))