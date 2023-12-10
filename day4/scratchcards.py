

def scratchcards(file):
    
    with open(file, 'r') as file_input:
        lines = [line.rstrip('\n') for line in file_input.readlines()]

    points_total = 0
    
    for line in lines:
        line = line[line.find(':') + 1:]
        numbers = line.split('|')
        wins_numbers = [int(number) for number in numbers[0].strip().split()]
        my_numbers = [int(number) for number in numbers[1].strip().split()]
        matches = 0
        
        for number in my_numbers:
            if number in wins_numbers:
                matches += 1
        
        points_total += int(2**(matches - 1))
        
    return points_total




def scratchcards_part_two(file):
    
    with open(file, 'r') as file_input:
        lines = [line.rstrip('\n') for line in file_input.readlines()]

    
    cards_instances = [1] * len(lines)
    
    for i, line in enumerate(lines):
        line = line[line.find(':') + 1:]
        numbers = line.split('|')
        wins_numbers = [int(number) for number in numbers[0].strip().split()]
        my_numbers = [int(number) for number in numbers[1].strip().split()]
        matches = 0
        
        for number in my_numbers:
            if number in wins_numbers:
                matches += 1
    
        for card_number in range(i + 1, min(i + matches + 1, len(cards_instances))):
            cards_instances[card_number] += cards_instances[i]
            
                
    return sum(cards_instances)









# Para la parte 1 
#print(scratchcards('input_test.txt'), scratchcards('input_test.txt') == 13,  13)
#print(scratchcards('input.txt'))


# Para la parte 2 
print(scratchcards_part_two('input_test.txt'), scratchcards_part_two('input_test.txt') == 30,  30)
print(scratchcards_part_two('input.txt'))
