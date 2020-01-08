# my-grep
Simple example of grep alternative 

usage: grep.py [-h] [-m N] [-i] [-s] [-t] FILE PATTERN

Search for PATTERN in FILE and displays line and frequency.

positional arguments:
  FILE                 path to the file to inspect
  PATTERN              a string to search

optional arguments:
  -h, --help           show this help message and exit
  -m N, --max-count N  stop after NUM selected lines
  -i, --ignore-case    ignore case distinctions
  -s, --show           displays the whole line with text
  -t, --total          displays total number of lines found
