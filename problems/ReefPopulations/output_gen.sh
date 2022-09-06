#!/bin/bash
for i in {0..13}
do
    python solutions/python3/main.py < tests/$i.in > tests/$i.out
done