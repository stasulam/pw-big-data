#!/usr/bin/bash
cat people-data.txt | python3 mapper.py | sort -k 1,1 | python3 reducer.py
