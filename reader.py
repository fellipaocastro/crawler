#!/usr/bin/env python
# coding: utf-8

import sys
import csv

try:
    with open(sys.argv[1], 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print ", ".join(row)
except IOError, e:
    print e
