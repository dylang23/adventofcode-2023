
class Cube:

    def __init__(self, color, quantity):
        self._color = color
        self._quantity = quantity

    @property
    def color(self):
        return self._color;


    @property
    def quantity(self):
        return self._quantity;


    def __str__(self):
        return f"{self._quantity}-{self._color}"




def cube_conundrum():
    
    with open('input.txt', 'r') as file_input:
        games_lines = [line.rstrip('\n') for line in file_input.readlines()]

    games = []

    for game_line in games_lines:
        game_line = game_line[game_line.find(':') + 1:]

        game = []
        for cubes_line in game_line.split(';'):
            cubes_line = cubes_line.strip()   
            
            attempt = []
            for cube in cubes_line.split(','):
                cube = cube.strip().split()
                attempt.append(Cube(cube[1], int(cube[0])))

            game.append(attempt)

        games.append(game)

    
    
    
    sum_ids = 0
    
    for game_id, game in enumerate(games):
        
        for attempt in game:
            
            failed_attempt = False

            for cube in attempt:                    
                if cube.color == 'red' and cube.quantity >  12:
                    failed_attempt = True
                    break
                
                if cube.color == 'green' and cube.quantity > 13:
                    failed_attempt = True
                    break
                
                if cube.color == 'blue' and cube.quantity > 14:
                    failed_attempt = True
                    break
        
            if failed_attempt:
                break
            
        if not failed_attempt:
            print(game_id+1)
            sum_ids += (game_id + 1)
            
    return sum_ids      
            

def cube_conundrum_part_two():
    
    with open('input.txt', 'r') as file_input:
        games_lines = [line.rstrip('\n') for line in file_input.readlines()]

    games = []

    for game_line in games_lines:
        game_line = game_line[game_line.find(':') + 1:]

        game = []
        for cubes_line in game_line.split(';'):
            cubes_line = cubes_line.strip()   
            
            attempt = []
            for cube in cubes_line.split(','):
                cube = cube.strip().split()
                attempt.append(Cube(cube[1], int(cube[0])))

            game.append(attempt)

        games.append(game)
        
        
    power_cube_sum = 0
    for game in games:
        
        minimum_number_cubes = [0, 0, 0]

        for attempt in game:
            for cube in attempt:                    
                if cube.color == 'red':
                    minimum_number_cubes[0] = max(cube.quantity, minimum_number_cubes[0])
                    
                if cube.color == 'green':
                    minimum_number_cubes[1] = max(cube.quantity, minimum_number_cubes[1])
                    
                if cube.color == 'blue':
                    minimum_number_cubes[2] = max(cube.quantity, minimum_number_cubes[2])
        
        power_cubes = 1
        for number in minimum_number_cubes:
            power_cubes = power_cubes * number
    
        power_cube_sum += power_cubes

    return power_cube_sum


print(cube_conundrum_part_two())