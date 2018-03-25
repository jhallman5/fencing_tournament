import sys
import csv
from linked_list import Node, Linked_List

with open(sys.argv[1], newline='') as csv_file:
    fencer_list = Linked_List()
    reader = csv.reader(csv_file, delimiter='\t')
    for row in reader:
        fencer = {
            'last_name': row[0].split(',')[0],
            'first_name': row[0].split(',')[1],
            'team': row[0].split(',')[2],
            'rank':row[0].split(',')[3]
            }
        fencer_list.insert(fencer)
    fencer_list.print_LL()
