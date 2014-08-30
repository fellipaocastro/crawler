#!/bin/bash

CSV_FILE="/tmp/ecp.csv"
LOG_FILE="/tmp/crawler-`date +%Y-%m-%d`.log"

case $1 in
    run)
        # rm $CSV_FILE >> $LOG_FILE 2>&1
        # scrapy crawl ecp -o $CSV_FILE >> $LOG_FILE 2>&1
        if [ -f $CSV_FILE ]; then
            TOTAL_ITEMS=$[$(wc -l < $CSV_FILE | sed -e 's/^[ \t]*//')-1]
            if [ $TOTAL_ITEMS -gt 0 ]; then
                echo "Stored csv feed ($TOTAL_ITEMS items) in: /tmp/ecp.csv"
            fi
        fi
        ;;
    check)
        flake8 . --verbose
        ;;
    *)
        echo "Crawler"
        echo ""
        echo "Usage:"
        echo "  ./manage.sh <command>"
        echo ""
        echo "Available commands:"
        echo "  run           Start the crawler"
        echo "  check         Run flake8 source code checker"
        ;;
 esac
