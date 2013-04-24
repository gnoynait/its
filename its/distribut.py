import csv
import sys
from collections import Counter

def static_distribution ():
    pswCnt = Counter ()
    reader = csv.reader (sys.stdin)
    for row in reader:
        for i in range (7, len (row), 2):
            pswCnt[row[i]] += 1
    return pswCnt

if __name__ == '__main__':
    pswCnt = static_distribution ()
    writer = csv.writer (sys.stdout)
    for passway, count in pswCnt.items ():
        writer.writerow ([passway, count])
