#!/usr/bin/env python

from operator import itemgetter
import sys

current_year = None
current_salary = 0
year = None

# read the entire line from STDIN
for line in sys.stdin:
    line = line.strip()
    # word, count = line.split('\t', 1)
    year, salary = line.split("\t", 1)
    try:
        salary = float(salary)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_year == year:
        current_salary += salary
    else:
        if current_year:
            # write result to STDOUT
            print(f"{current_year}: {current_salary:.2f}")
        current_salary = salary
        current_year = year

# do not forget to output the last word if needed!
if current_year == year:
    print(f"{current_year}: {current_salary:.2f}")
