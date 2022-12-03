#!/bin/bash
set -euo pipefail

score=0
while read -r opponent response; do
    score=$(( score + "$response" ))
    if [[ $response == "1" && $opponent == "3" ]] || [[ $response == "3" && $opponent == "2" ]] || [[ $response == "2" && $opponent == "1" ]]; then
        # win
        score=$(( score + 6 ))
    elif [ "$opponent" -eq "$response" ]; then
        # draw
        score=$(( score + 3 ))
    fi
done < <(sed -E -e 's/(X|A)/1/g' -e 's/(Y|B)/2/g' -e 's/(Z|C)/3/g' inputs/02)

echo "Part 1: $score"

score=0
while read -r opponent outcome; do
    score=$(( score + "$outcome" ))
    case $outcome in
    0)
        case $opponent in
        A)
        score=$(( score + 3 ))
        ;;
        B)
        score=$(( score + 1 ))
        ;;
        C)
        score=$(( score + 2 ))
        ;;
        esac
        ;;
    3)
        case $opponent in
        A)
        score=$(( score + 1 ))
        ;;
        B)
        score=$(( score + 2 ))
        ;;
        C)
        score=$(( score + 3 ))
        ;;
        esac
        ;;
    6)
        case $opponent in
        A)
        score=$(( score + 2 ))
        ;;
        B)
        score=$(( score + 3 ))
        ;;
        C)
        score=$(( score + 1 ))
        ;;
        esac
        ;;
    esac
done < <(sed -e 's/X/0/g' -e 's/Y/3/g' -e 's/Z/6/g' inputs/02)

echo "Part 2: $score"
