#Tyfabian Williams
#2142655


lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))

print()
print(f'Lemonade ingredients - yields {servings:.2f} servings')
print(f'{lemon_juice_cups:.2f} cup(s) lemon juice')
print(f'{water_cups:.2f} cup(s) water')
print(f'{agave_nectar_cups:.2f} cup(s) agave nectar')
print()

new_serv = float(input('How many servings would you like to make?\n'))
serving_convert = new_serv / servings
print()
print(f'Lemonade ingredients - yields {new_serv:.2f} servings')
print(f'{lemon_juice_cups * serving_convert:.2f} cup(s) lemon juice')
print(f'{water_cups * serving_convert:.2f} cup(s) water')
print(f'{agave_nectar_cups * serving_convert:.2f} cup(s) agave nectar')
print()

cups_to_gallons = 1 / 16

print(f'Lemonade ingredients - yields {new_serv:.2f} servings')
print(f'{lemon_juice_cups * serving_convert * cups_to_gallons:.2f} gallon(s) lemon juice')
print(f'{water_cups * serving_convert * cups_to_gallons:.2f} gallon(s) water')
print(f'{agave_nectar_cups * serving_convert * cups_to_gallons:.2f} gallon(s) agave nectar')
