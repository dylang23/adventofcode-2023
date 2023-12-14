def oasis(file):
        
    with open(file, 'r') as file_input:
        lines = [line.rstrip('\n') for line in file_input.readlines()]

    sum_prediction = 0
    for history in lines:
        history = [int(value) for value in history.split()]
        last_values = [] 

        while not all(value == 0 for value in history):
            for index in range(0, len(history) - 1):
                history[index] = history[index + 1] - history[index]            
            
            last_values.append(history.pop())            
            
        sum_prediction += sum(last_values)

    return sum_prediction
        
        
#TEST PARA LA PRIMERA PARTE

# print(oasis('input_test1.txt'), 114)
# print(oasis('input_test2.txt'), 2174807968)
# print(oasis('input.txt'), 2038472161)


from functools import reduce

def oasis_part_two(file):
        
    with open(file, 'r') as file_input:
        lines = [line.rstrip('\n') for line in file_input.readlines()]

    prediction = 0
    
    for history in lines:
        history = [int(value) for value in history.split()]
        first_values = [history[0]] 

        while not all(value == 0 for value in history):
            for index in range(0, len(history) - 1):
                history[index] = history[index + 1] - history[index]            
                
            first_values.append(history[0])
            history.pop()            
            
        prediction_history = 0
        for i in range(0, len(first_values) - 1, 2):
            prediction_history += first_values[i] - first_values[i + 1]
            
        prediction += prediction_history

    return prediction

print(oasis_part_two('input_test_part_two.txt'), 5)
print(oasis_part_two('input_test2.txt'), 1208)
print(oasis_part_two('input.txt'), 1091)