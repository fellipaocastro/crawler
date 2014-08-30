#!/bin/bash

CSV_FILE="/tmp/ecp.csv"
LOG_FILE="/tmp/crawler-`date +%Y-%m-%d`.log"

case $1 in
    run)
        rm $CSV_FILE >> $LOG_FILE 2>&1
        scrapy crawl ecp -o $CSV_FILE >> $LOG_FILE 2>&1
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
