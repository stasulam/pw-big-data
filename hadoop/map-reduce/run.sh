#!/usr/bin/bash
hadoop-streaming \
    -input /tmp/pw312/people-data.txt \
    -output /tmp/pw312/output/ \
    -mapper ./mapper.py \
    -reducer ./reducer.py \
    -file ./reducer.py \
    -file ./mapper.py
