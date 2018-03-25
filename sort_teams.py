import sys
import csv
from linked_list import Node

with open(sys.argv[1], newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter='\t')
    for row in reader:
        fencer = {
            'last_name': row[0].split(',')[0],
            'first_name': row[0].split(',')[1],
            'team': row[0].split(',')[2],
            'rank':row[0].split(',')[3]
            }
        node = Node(fencer)
        print(node.data)
