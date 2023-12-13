from math import lcm


def get_input(file):
    
    with open(file, 'r') as file_input:
        lines = [line.rstrip('\n') for line in file_input.readlines()]

    instructions = lines[0]
    lines = lines[2:] 
    network = {}
    
    for node in lines:
        tag_node = node[:node.find('=')].rstrip()
        open_parrent = node.find('(')
        close_parrent = node.find(')')
        childs = node[open_parrent + 1:close_parrent].split(',') 
        tag_left = childs[0].strip()
        tag_right = childs[1].strip()   
        network[tag_node] = (tag_left, tag_right)
        
    return (instructions, network)


def networks(file):
    
    instructions, network = get_input(file)
    steps = 0
    node = 'AAA'
    
    while node != 'ZZZ':
        
        for instruction in instructions:
        
            if instruction == 'L':
                node = network[node][0]
        
            if instruction == 'R':
                node = network[node][1]
            
            steps += 1
                    
            if node == 'ZZZ':
                return steps


def get_input(file):
    
    with open(file, 'r') as file_input:
        lines = [line.rstrip('\n') for line in file_input.readlines()]

    instructions = lines[0]
    lines = lines[2:] 
    network = {}
    nodes_ending_a = []
    for node in lines:
        tag_node = node[:node.find('=')].rstrip()
        open_parrent = node.find('(')
        close_parrent = node.find(')')
        childs = node[open_parrent + 1:close_parrent].split(',') 
        tag_left = childs[0].strip()
        tag_right = childs[1].strip()   
        network[tag_node] = (tag_left, tag_right)
        
        if tag_node[2] == 'A':
            nodes_ending_a.append(tag_node)
        
                
    return (instructions, network, nodes_ending_a)

def networks_part_two(file):
    
    instructions, network, nodes_ending_a = get_input(file)
    steps = 0
    check_steps_minimum = False
    steps_minimum_ending_a = [0] * len(nodes_ending_a)
    
    while not check_steps_minimum:

        for instruction in instructions:
            new_node_ending_a = []
            steps += 1
            
            for node_ending_a in nodes_ending_a: 
        
                if instruction == 'L':
                    node = network[node_ending_a][0]

                if instruction == 'R':
                    node = network[node_ending_a][1]

                new_node_ending_a.append(node)
            
            nodes_ending_a = new_node_ending_a
            
            for i, node in enumerate(nodes_ending_a):
                if node[2] == 'Z':
                    steps_minimum_ending_a[i] = steps
            
        check_steps_minimum = all(step != 0 for step in steps_minimum_ending_a) 

    
    return lcm(*steps_minimum_ending_a)


        
### TEST PARA LA PRIMERA PARTE

# print(networks('input_test.txt'), 2)
# print(networks('input_test2.txt'), 6)
# print(networks('input_test3.txt'), 17873)
# print(networks('input.txt'), 15989)


### TEST PARA LA SEGUNDA PARTE
print(networks_part_two('input_test_part_two.txt'), 6)
print(networks_part_two('input_test3.txt'), 15746133679061)
print(networks_part_two('input.txt'), 13830919117339)



