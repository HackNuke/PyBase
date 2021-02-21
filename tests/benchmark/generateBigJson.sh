#!/bin/bash
# Thanks to Nestor Urquiza per doing this useful json stress generator
# https://thinkinginsoftware.blogspot.com/2013/02/create-big-json-file-for-test-purposes.html
#
# Usage and warnings
# ==================
# MAX is the number of lines that our stress json file will have,
# you can put as many lines as you want.
#
# WARNING: We do not recommend placing more than 100k lines so as
# not to make the code editor "convulse".
#
# Usage:
# 1. ./generateBigJson.sh >> stress.json
# 2. After doing it, copy all the file content and paste it into a new 
# benchmark function inside the benchmark.py file and then just run it.
MAX=30000
echo "{\"arr\":["
i=1
while [ $i -le $MAX ]; do
  echo -ne "{\"id\":$i, \"next\":$((i+1))}"
  if [ "$i" -ne "$MAX" ]; then
    echo ","
  fi
  let i=i+1
done
echo "]}"
