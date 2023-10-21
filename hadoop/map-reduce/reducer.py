#!/usr/bin/python3

from operator import itemgetter
import sys

current_year = None
current_count = 0
current_salary = 0
year = None

for line in sys.stdin:
    line = line.strip()
    year, salary, count = line.split("\t")
    try:
        salary = float(salary)
        count = int(count)
    except ValueError:
        continue

    if current_year == year:
        current_salary += salary
        current_count += count
    else:
        if current_year:
            print(f"{current_year}: {current_salary / current_count:.2f}")
        current_salary = salary
        current_count = count
        current_year = year

if current_year == year:
    print(f"{current_year}: {current_salary / current_count:.2f}")
