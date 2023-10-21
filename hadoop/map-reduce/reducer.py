#!/usr/bin/env python

from operator import itemgetter
import sys

current_year = None
current_salary = 0
year = None

for line in sys.stdin:
    line = line.strip()
    year, salary = line.split("\t", 1)
    try:
        salary = float(salary)
    except ValueError:
        continue

    if current_year == year:
        current_salary += salary
    else:
        if current_year:
            print(f"{current_year}: {current_salary:.2f}")
        current_salary = salary
        current_year = year

if current_year == year:
    print(f"{current_year}: {current_salary:.2f}")
