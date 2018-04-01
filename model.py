import sys
import csv
from linked_list import Node, Linked_List

def create_linked_list():
    ''' Creates a sorted linked list from a CSV file. '''
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
        return fencer_list

def determine_num_pools(linked_list):
    ''' Returns the number of pools. '''
    Num_fencers = number_of_participates(linked_list)
    if check_pool_size(Num_fencers, 6):
        return int(Num_fencers / 6)
    if check_pool_size(Num_fencers, 7):
        return int(Num_fencers / 7)
    if check_pool_size(Num_fencers, 5):
        return int(Num_fencers / 5)

def number_of_participates(linked_list):
    ''' Returns the number of participates. '''
    current = linked_list.head
    count = 1
    while current.next_node:
        count += 1
        current = current.next_node
    return count

def check_pool_size(num_fencers, proposed_pool_size):
    '''
        Determines how many pools there will be of the proposed size.
        Determines remaining fencers.
        Returns boolean: if remaining fencers can fit into number of pools.
     '''
    number_of_pools = int(num_fencers / proposed_pool_size)
    remaining_fencers = num_fencers % (number_of_pools * proposed_pool_size)
    if remaining_fencers / number_of_pools <= 1 :
        return True
    return False

def create_init_pools(linked_list, num_pools):
    ''' Returns a list of initial pools of equal difficulty using serpentine method. '''
    sorted_list = []
    init_pools = []
    for i in range(0, num_pools):
        init_pools.append([])
    current_node = linked_list.head
    direction_forward = False
    while current_node:
        sorted_list.append(current_node.data)
        current_node = current_node.next_node
    for index, fencer in enumerate(sorted_list):
        if sorted_list.index(fencer) % num_pools == 0:
            direction_forward = not direction_forward
        if direction_forward:
            init_pools[index % num_pools].append(fencer)
        else:
            init_pools[(num_pools - 1) - (index % num_pools)].append(fencer)
    # print('Pool 1 ---> ', init_pools[0])
    # print('-------------')
    # print('Pool 2 ---> ', init_pools[1])
    # print('-------------')
    # print('Pool 3 ---> ', init_pools[2])
    # print('-------------')
    # print('Pool 4 ---> ', init_pools[3])
    count_team_members_per_pool(init_pools)
    return init_pools

def count_team_members_per_pool(init_pools):
    teams_dict = {}
    for pool in init_pools:
        pool_dict = {}
        for player in pool:
            if player.get('team'):
                if not pool_dict.get(player.get('team')):
                    pool_dict[player.get('team')] = 1
                else:
                    pool_dict[player.get('team')] += 1
                print(player.get('team'))
            else:
                print('NULL')
        print(pool_dict)
