#!/bin/bash

for file in *.py; do 
  name=$(basename "$file" .py)
  mv "$file" "$name.txt"
done
