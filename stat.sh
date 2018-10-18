#!/bin/bash
if [ -f stat.txt ]; then
    rm stat.txt;
fi

git log --after="$1" --before="$2" --no-merges --stat | grep insertion >> stat.txt