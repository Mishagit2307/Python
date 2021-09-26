#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#This program finds roots quadratic equation a*x**2 + b*x + c = 0.


import math

abc_index = list(map(float, input("Enter a, b, c index for quadratic equation, comma separated: ").split(",")))

def finding_discriminant(a,b,c):
    d = b ** 2 - 4 * a * c
    return d

discriminant = finding_discriminant(abc_index[0], abc_index[1], abc_index[2])
if discriminant > 0:
    print("The equation has two roots.")
    try:
        root_1 = (-(abc_index[1]) + math.sqrt(discriminant))/(2 * abc_index[0])
        root_2 = (-(abc_index[1]) - math.sqrt(discriminant))/(2 * abc_index[0])
    except ZeroDivisionError:
        print("Index a != 0 !!!")
    try:
        print(f"x_1 = {root_1} and x_2 = {root_2}" )
    except NameError:
        print(f"x_1 = x_2 = {-abc_index[2]/abc_index[1]}")
elif discriminant == 0:
    print("The equation has one roots.")
    root_1 = (-(abc_index[1]))/(2 * abc_index[0])
    print(f"x_1 = x_2 = {root_1}" )
else:
    print("The equation has no roots in the field of real numbers.")
