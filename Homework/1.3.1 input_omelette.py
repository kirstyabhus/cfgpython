eggs_in_a_box = 6
eggs_for_an_omelette = 4

no_of_boxes = 3
# code in comment asks user for input instead
# no_of_boxes = int(input("How many boxes of eggs do you have?"))
total_eggs = eggs_in_a_box * no_of_boxes

total_omelettes = total_eggs // eggs_for_an_omelette

print(f"You can make {total_omelettes} omelettes with {no_of_boxes} boxes of eggs.")

