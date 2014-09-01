#!/bin/bash

CSV_FILE="/tmp/ecp.csv"
LOG_FILE="/tmp/crawler-`date +%Y-%m-%d`.log"
ROOT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

case $1 in
    setup)
        pip install -r $ROOT_PATH/requirements.txt
        ;;
    run)
        rm $CSV_FILE >> $LOG_FILE 2>&1
        scrapy crawl ecp -o $CSV_FILE >> $LOG_FILE 2>&1
        if [ -f $CSV_FILE ]; then
            TOTAL_ITEMS=$[$(wc -l < $CSV_FILE | sed -e 's/^[ \t]*//')-1]
            if [ $TOTAL_ITEMS -gt 0 ]; then
                echo "Stored csv feed ($TOTAL_ITEMS items) in: $CSV_FILE"
            fi
        fi
        ;;
    read)
        .$ROOT_PATH/reader.py $CSV_FILE
        ;;
    log)
        tail -F $LOG_FILE
        ;;
    test)
        nosetests --with-spec --spec-color crawler.tests
        ;;
    check)
        flake8 $ROOT_PATH --verbose
        ;;
    *)
        echo "Crawler"
        echo ""
        echo "Usage:"
        echo "  ./manage.sh <command>"
        echo ""
        echo "Available commands:"
        echo "  setup         Install dependencies"
        echo "  run           Start the crawler"
        echo "  read          Read the generated csv file"
        echo "  log           Tail the log file"
        echo "  test          Run the test suit"
        echo "  check         Run flake8 source code checker"
        ;;
 esac
