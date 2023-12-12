from functools import cmp_to_key

def type_hand(hand):

	labels_repeat = {'J': 0}
	labels_distinct = 0

	for label in hand:
		if not label in labels_repeat and label != 'J':
			labels_repeat[label] = 1
			labels_distinct += 1
			continue 
	   
		labels_repeat[label] += 1

	card_max_repeat = labels_repeat[max(labels_repeat, key=lambda k: labels_repeat.get(k) if k != 'J' else float('-inf'))]

	if labels_repeat['J'] > 0:
		jokers_label = labels_repeat['J']
		
		if labels_distinct >= 1: 
			card_max_repeat += jokers_label

	if card_max_repeat == 5:
		return 7
	
	elif card_max_repeat == 4:
		return 6
	
	elif card_max_repeat == 3 and labels_distinct == 2:
		return 5
	
	elif card_max_repeat == 3 and labels_distinct == 3:
		return 4
	
	elif card_max_repeat == 2 and labels_distinct == 3:
		return 3
	
	elif card_max_repeat == 2 and labels_distinct == 4:
		return 2
	
	return 1

## Si hand es mayor a other_hand entonces retorna 1
## Si hand es igual a other_hand entonces retorna 0
## Si hand es menor a other_hand entonces retorna -1

def hand_stronge(hand, other_hand):
	
	labels_strength = { 'A' : 13, 'K' : 12, 'Q' : 11, 'T' : 10, '9' : 9, '8' : 8, '7' : 7, '6' : 6, '5' : 5, '4' : 4, '3' : 3, '2' : 2, 'J' : 1 }
	
	for label, label_other in zip(hand, other_hand):
		if labels_strength[label] > labels_strength[label_other]:
			return 1

		if labels_strength[label] < labels_strength[label_other]:
			return -1
		
	return 0


def hand_compare(hand1, hand2):

	type_hand1 = type_hand(hand1[0])
	type_hand2 = type_hand(hand2[0])

	if type_hand1 > type_hand2:
		return 1
	
	if type_hand1 < type_hand2:
		return -1

	hand_stronged = hand_stronge(hand1[0], hand2[0])

	return hand_stronged



def camel_cards(file):

	with open(file, 'r') as file_input:
		lines = [line.rstrip('\n') for line in file_input.readlines()]

	hands_bid = []
	for line in lines:
		hand = line.split()
		hand_bid = (hand[0], int(hand[1]))
		hands_bid.append(hand_bid)

	hands_bid = sorted(hands_bid, key=cmp_to_key(hand_compare))
	winnings = 0

	for rank, hand_bind in enumerate(hands_bid):
		winnings += hand_bind[1] * (rank + 1)

	return winnings



#print(type_hand('23456'))

# print(camel_cards('input_test.txt'))
print(camel_cards('input.txt'))
# print(compare_hand('KK677', 'KTJJT'))

