

def input_gear_ratios():
    with open('input.txt', 'r') as file_input:
        lines = [line.rstrip('\n') for line in file_input.readlines()]

    engine_matrix = []
    
    for line in lines:
        engine_row = []
        
        for character in line:
            engine_row.append(character)
        
        engine_matrix.append(engine_row)
    
    
    return engine_matrix


def is_partnumber(engine_matrix, number_location):


    row = number_location[0]
    column_ini = number_location[1]
    column_fin = number_location[2]

    adyacentLocations = [[0, -1], [0, 1], [-1, -1], [1, -1], [-1, 1], [1, 1]]

    for adyacentLocation in adyacentLocations:
        
        adyacentLocation_x = adyacentLocation[0]
        adyacentLocation_y = adyacentLocation[1]

        # column_ini - 1 >= 0
        # column_fin + 1 < len(engine_matrix)
        # row - 1 >= 0
        # row + 1 < len(engine_matrix)

    if column_ini - 1 >= 0:
        if engine_matrix[row][column_ini - 1] != '.':
            return True
    
    if column_fin + 1 < len(engine_matrix):
        if engine_matrix[row][column_fin + 1] != '.': 
            return True
        
        
    for j in range(column_ini, column_fin + 1):
        
        if row - 1 >= 0:
            if engine_matrix[row-1][j] != '.':
                return True
        
        if row + 1 < len(engine_matrix):
            if engine_matrix[row + 1][j] != '.':
                return True
        
    
    if row - 1 >= 0 and column_ini - 1 >= 0:
        if engine_matrix[row - 1][column_ini - 1] != '.' and not engine_matrix[row - 1][column_ini - 1].isdigit():
            return True 
        
    if row + 1 < len(engine_matrix) and column_ini - 1 >= 0:
        if engine_matrix[row + 1][column_ini - 1] != '.' and not engine_matrix[row + 1][column_ini - 1].isdigit():
            return True
        
    if row - 1 >= 0 and column_fin + 1 < len(engine_matrix):
        if engine_matrix[row - 1][column_fin + 1] != '.' and not engine_matrix[row - 1][column_ini + 1].isdigit():
            return True
            
    if row + 1 < len(engine_matrix) and column_fin + 1 < len(engine_matrix):
        if engine_matrix[row + 1][column_fin + 1] != '.' and not engine_matrix[row + 1][column_ini + 1].isdigit():
            return True
     
    
    return False
    
def getLocationWear(engine_matrix, number_location):


    row = number_location[0]
    column_ini = number_location[1]
    column_fin = number_location[2]


    if column_ini - 1 >= 0:
        if engine_matrix[row][column_ini - 1] == '*':
            return [row, column_ini - 1]
    
    if column_fin + 1 < len(engine_matrix):
        if engine_matrix[row][column_fin + 1] == '*': 
            return [row, column_fin + 1]
        
        
    for j in range(column_ini, column_fin + 1):
        
        if row - 1 >= 0:
            if engine_matrix[row-1][j] == '*':
                return [row-1, j]
        
        if row + 1 < len(engine_matrix):
            if engine_matrix[row + 1][j] == '*':
                return [row + 1, j]
        
    
    if row - 1 >= 0 and column_ini - 1 >= 0:
        if engine_matrix[row - 1][column_ini - 1] == '*' and not engine_matrix[row - 1][column_ini - 1].isdigit():
             return [row - 1, column_ini - 1]
        
    if row + 1 < len(engine_matrix) and column_ini - 1 >= 0:
        if engine_matrix[row + 1][column_ini - 1] == '*' and not engine_matrix[row + 1][column_ini - 1].isdigit():
            return [row + 1, column_ini - 1]
        
    if row - 1 >= 0 and column_fin + 1 < len(engine_matrix):
        if engine_matrix[row - 1][column_fin + 1] == '*' and not engine_matrix[row - 1][column_ini + 1].isdigit():
            return [row - 1, column_fin + 1]
            
    if row + 1 < len(engine_matrix) and column_fin + 1 < len(engine_matrix):
        if engine_matrix[row + 1][column_fin + 1] == '*' and not engine_matrix[row + 1][column_ini + 1].isdigit():
            return [row + 1, column_fin + 1]
     
    
    return None
    
def gear_ratios():
    
    engine_matrix = input_gear_ratios()
    number_part_total = 0 
    
    for i, engine_row in enumerate(engine_matrix):
        number_location = None
        number_locations = []
        
        for j, elem in enumerate(engine_row):

            if elem.isdigit(): 

                if number_location is None:
                    number_location = [i, j, j]

                else:
                    number_location[2] = j
            
            else:
                
                if not number_location is None:
                    number_locations.append(number_location)
                    number_location = None
                 
        if not number_location is None:
            number_locations.append(number_location)
        
        for number_location in number_locations:
            number = 0
            
            for j in range(number_location[1], number_location[2] + 1):
                number = number * 10 + int(engine_matrix[number_location[0]][j])
                
            print(number)
            if is_partnumber(engine_matrix, number_location):
                #print(number)
                number_part_total += number
            else:
                pass
                # print(number)

    
    return number_part_total



def gear_ratios_part_two():
            
    engine_matrix = input_gear_ratios()
    number_part_total = 0 
    wear_locations = {}
    gear_ratio_total = 0
    
    for i, engine_row in enumerate(engine_matrix):
        number_location = None
        number = 0
        for j, elem in enumerate(engine_row):

            if elem == '*' and (i, j) not in wear_locations:
                wear_locations[(i, j)] = []

            if elem.isdigit(): 
                number = number * 10 + int(elem)
                if number_location is None:
                    number_location = [i, j, j]
                    
                else:
                    number_location[2] = j
            
            else:
                if not number_location is None:
                    locationSysmbol = getLocationWear(engine_matrix, number_location)
                    if not locationSysmbol is None:
                        # print(locationSysmbol)
                        if (locationSysmbol[0], locationSysmbol[1]) in wear_locations:
                            wear_locations[(locationSysmbol[0], locationSysmbol[1])].append(number)
                        else:
                            wear_locations[(locationSysmbol[0], locationSysmbol[1])] = [number]
                    
                number_location = None
                number = 0
         
        if not number_location is None:
            locationSysmbol = getLocationWear(engine_matrix, number_location)
            if not locationSysmbol is None:
                # print(locationSysmbol)
                if (locationSysmbol[0], locationSysmbol[1]) in wear_locations:
                    wear_locations[(locationSysmbol[0], locationSysmbol[1])].append(number)
                else:
                    wear_locations[(locationSysmbol[0], locationSysmbol[1])] = [number]

        for clave, valor in wear_locations.items():
            gear_ratio = 1
            if len(valor) == 2:
                gear_ratio = valor[0] * valor[1]
                print(clave,valor)
                gear_ratio_total += gear_ratio
                wear_locations[clave] = []

        
    return gear_ratio_total


#print(gear_ratios(), 509115)
print(gear_ratios_part_two())



