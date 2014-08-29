#!/bin/bash

case $1 in
    run)
        rm ecp.csv &> /dev/null
        scrapy crawl ecp -o ecp.csv
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
