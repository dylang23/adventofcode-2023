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
    
    
    

print(seeds('input_test.txt'))
print(seeds('input.txt'))