#!/usr/bin/python3 

def trebuchet():
    
    with open('input.txt', 'r') as file_input:
        lines = [line.rstrip('\n') for line in file_input.readlines()]

    calibration_total = 0
    
    for line in lines:
        calibration_value = 1
        for caracter in line:
            if caracter.isdigit():
                if calibration_value == 1: 
                    calibration_value = int(caracter) * 10 + int(caracter)
                else:
                    calibration_value = (calibration_value // 10) * 10 + int(caracter)
        
        calibration_total += calibration_value

    return calibration_total

def letter_to_digit(digit_letter):
    digit_letters = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    return digit_letters[digit_letter]

def is_digit_letter(posible_digit):

    digit_letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    return posible_digit in digit_letters


def trebuchet_part2():
    
    with open('input.txt', 'r') as file_input:
        lines = [line.rstrip('\n') for line in file_input.readlines()]

    calibration_total = 0
    
    for line in lines:
        calibration_value = 1

        for index, caracter in enumerate(line):
            digit = -1
            
            if caracter.isdigit():
                digit = int(caracter)
            
            for j in range(3, 6):
                possible_digit = line[index:(index + j)]
                if is_digit_letter(possible_digit):
                    digit = letter_to_digit(possible_digit)

            if digit != -1:
                if calibration_value == 1: 
                    calibration_value = digit * 10 + digit
                else:
                    calibration_value = (calibration_value // 10) * 10 + digit
        
        calibration_total += calibration_value

    return calibration_total

print(trebuchet_part2(), trebuchet_part2()==54676)