#!/bin/bash

analyzesize() {
echo "Анализ размера каждой папки и файла в текущей папке:"
echo "===================================================="

sizexxx=()

for xxx in *; do

if [ -e "$xxx" ]; then
size=$(du -sh "$xxx" 2>/dev/null | cut -f1)
echo "$size $xxx"
fi

done | sort -rh
}


analyzesize

