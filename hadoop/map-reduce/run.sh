#!/usr/bin/bash
dt=`date +%Y%m%d-%H%M%S`

hadoop-streaming \
    -D mapreduce.jobs.reduces=4 \
    -input /tmp/pw312/people-data.txt \
    -output /tmp/pw312/output/$dt/ \
    -mapper ./mapper.py \
    -reducer ./reducer.py \
    -file ./reducer.py \
    -file ./mapper.py
