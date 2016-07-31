#!/bin/bash
tr -s " " < lastb.txt | cut -d" " -f1,3 | uniq -c -d | tr -s " " | sort -t" " -k1 -n | sort | uniq -c | tr -s " " | sort -n
