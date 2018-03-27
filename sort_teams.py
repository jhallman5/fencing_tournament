import sys
import csv
from linked_list import Node, Linked_List
from model import create_linked_list, determine_num_pools, create_init_pools

LL = create_linked_list()
num_pools = determine_num_pools(LL)
create_init_pools(LL, num_pools)
