#!/bin/bash

rm ecp.csv &> /dev/null
scrapy crawl ecp -o ecp.csv
