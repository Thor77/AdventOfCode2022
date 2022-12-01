#!/bin/bash
set -euo pipefail

tmp=$(mktemp)
tmp_sorted="${tmp}.sorted"
current=0
while read -r line; do
    if [ -z "$line" ]; then
        echo $current >> "$tmp"
        current=0
    else
        current=$(( current + line ))
    fi
done < inputs/01
echo $current >> "$tmp"

sort -r "$tmp" > "$tmp_sorted"

echo "Part 1: $(head -n1 "$tmp_sorted")"
echo "Part 2: $(head -n3 "$tmp_sorted" | paste -sd+ | bc)"

rm "$tmp" "$tmp_sorted"
