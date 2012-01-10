#!/bin/bash
BOTH=`grep "$2" "$1" | grep "$3" | sort | cut -c1-4 | uniq -c | awk  '{print$2, $1,"\x27" "'"$2","$3"'""\x27"}'`
FIRST=`grep "$2" "$1" | sort | cut -c1-4 | uniq -c | awk '{print$2, $1, "\x27""'"$2"'""\x27"}'`
SECOND=`grep "$3" "$1" | sort | cut -c1-4 | uniq -c | awk '{print$2, $1, "\x27""'"$3"'""\x27"}'`

echo "Year" "Frequency" "Subject"
echo "$FIRST\n$SECOND\n$BOTH" | sort
