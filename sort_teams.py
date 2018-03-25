import sys
import csv

with open(sys.argv[1], newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter='\t')
    for row in reader:
        print(', '.join(row))
