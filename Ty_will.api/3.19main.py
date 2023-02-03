#Tyfabian Williams
#2142655

import math




user_height = float(input('Enter wall height (feet):\n'))
user_width = float(input('Enter wall width (feet):\n'))

wall_area = user_height * user_width
print(f'Wall area: {wall_area:.2f} square feet')

square_foot_per_gallon = 350
gallons_needed = wall_area / square_foot_per_gallon
cans_needed = math.ceil(gallons_needed)

print(f'Paint needed: {gallons_needed:.2f} gallons')
print(f'Cans needed: {cans_needed} can(s)')
print()

paint_color = input('Choose a color to paint the wall:\n')

blue_p = 25
red_p = 35
green_p = 23
if paint_color == 'red':
    print(f'Cost of purchasing red paint: ${red_p * cans_needed}')
elif paint_color == 'blue':
    print(f'Cost of purchasing blue paint: ${red_p * cans_needed}')
elif paint_color == 'green':
    print(f'Cost of purchasing green paint: ${red_p * cans_needed}')

