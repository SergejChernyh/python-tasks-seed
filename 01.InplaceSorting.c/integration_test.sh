#!/bin/bash

status=true

# ---------------------------------------------------

input="5 1 4 2 8"

result=$(uv run python -O ./sorting_demo.py $input)

expected=$(echo $input | xargs -n1 | sort -n | xargs)

while read -r line; do
    if [ -z "$line" ]; then continue; fi
    func_name=$(echo "$line" | cut -d' ' -f1)
    output=$(echo "$line" | cut -d' ' -f2- | xargs)

    if [ "$output" == "ERROR" ]; then
        echo "$func_name: ERROR"
        status=false
    elif [ "$output" == "$expected" ]; then
        echo "$func_name: OK"
    else
        echo "$func_name: FAILED"
        status=false
    fi
done <<< "$result"

# ---------------------------------------------------

$status
