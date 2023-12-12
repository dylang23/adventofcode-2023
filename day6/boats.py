from math import sqrt

def boats(races):

    count_beat_record = 1
    for (time, distance) in races:

        minimum_hold_time = int((time - sqrt(time**2 - 4 * distance)) / 2) + 1
        maximun_hold_time = int((time + sqrt(time**2 - 4 * distance)) / 2) 

        if (time - maximun_hold_time) * maximun_hold_time == distance:
            maximun_hold_time -= 1

        count_beat_record *= (maximun_hold_time - minimum_hold_time) + 1

    return count_beat_record


## TEST PARA LA PRIMERA PARTE

races_test1 = [(7,  9), (15, 40), (30,200)]
races_test2 = [(45,  305), (97, 1062), (72,1110), (95, 1695)]
races_test3 = [(59,  597), (79, 1234), (65,1032), (75, 1328)]
races_input = [(52,  426), (94, 1374), (75,1279), (94, 1216)]
#print(boats(races_test3))    


## TEST PARA LA SEGUNDA PARTE


races = [(52947594, 426137412791216)]
print(boats(races), 33149631)
