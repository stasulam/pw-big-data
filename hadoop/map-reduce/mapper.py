#!/usr/bin/env python 
import re
import sys 


for line in sys.stdin:
    line = line.strip()
    words = line.split(",")
    year, salary = (
        re.search("[0-9]{4}", words[0]).group(0),
        float(re.sub("\$", "", words[-1])),
    )
    print(f"{year}\t{salary}")
