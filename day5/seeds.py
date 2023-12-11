from sys import maxsize
from numpy import arange

def input_file(file):

    with open(file, 'r') as file_input:
        lines = [line.rstrip('\n') for line in file_input.readlines()]
        

    seeds_input = lines[0]
    seeds = [int(seed) for seed in seeds_input[seeds_input.find(':') + 1:].strip().split()]
    
    lines = lines[3:]
    maps = []
    
    for _ in range(7):
        
        category = []    
        j = 0
 
        for list_number in lines:
            if list_number == '':
                break
            
            j += 1
            category_row = [int(number) for number in list_number.split()]
            category.append(category_row)
    
        maps.append(category)
        lines = lines[j + 2:]
    
    return seeds, maps
    
            
def convert(maps, number, category_id):
    
    for list_number in maps[category_id]:
        source_range_start = list_number[1]
        range_length = list_number[2]
        if number >= source_range_start and number <= source_range_start + (range_length - 1):
            return list_number[0] + abs(number - source_range_start) 

    return number

def seeds(file):
    
    seeds , maps = input_file(file)
    numbers_convert = []
    
    for seed in seeds:
        number_convert = seed

        for j in range(7):
            number_convert = convert(maps, number_convert, j)   
            
        
        numbers_convert.append(number_convert)
        
    return min(numbers_convert)
    
    
def seeds_part_two(file):
    seeds , maps = input_file(file)

    seeds_range = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]  

    lowest_location = maxsize
    for seed_range in seeds_range:

        seed = seed_range[0]
        seed_final = seed_range[0] + seed_range[1]
        while seed < seed_final:
            number_convert = seed
            
            salto = maxsize
            for j in range(7):
                 flag = False
                 for list_number in maps[j]:
                    source_range_start = list_number[1]
                    range_length = list_number[2]
                    if number_convert >= source_range_start and number_convert <= source_range_start + (range_length - 1):
                        salto = min(salto, source_range_start + (range_length - 1) - number_convert)
                        number_convert = list_number[0] + abs(number_convert - source_range_start)
                        # print(j, seed, number_convert) 
                        flag = True
                        break
                 if not flag:
                    pass
                    #  print(j, seed, number_convert)   
            print(seed, salto)
            seed += salto + 1
            lowest_location = min(lowest_location, number_convert)

    return lowest_location


    # print(seeds_range)


# TEST PARA LA PRIMERA PARTE

# print(seeds('input_test.txt'))
# print(seeds('input.txt'))



# TEST PARA LA SEGUNDA PARTE

# print(seeds_part_two('input_test.txt'))
#print(seeds_part_two('input_test.txt'), seeds_part_two('input_test.txt') == 46, 46)
print(seeds_part_two('input.txt'), 11611182)









