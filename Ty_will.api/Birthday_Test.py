# Tyfabian Williams
# 2142566


birthday = input('What is your birthday?, ex. "03/12/2004".\n')
current_date = input('What is today\'s date in ex. "03/12/2004".\n')

birth_list = birthday.split("/")
date_list = current_date.split('/')

birth_ints = []
date_ints = []

for num in birth_list:
    birth_ints.append(int(num))
for num in date_list:
    date_ints.append(int(num))

age = date_ints[-1] - birth_ints[-1]

print(f'Current day\nMonth: {date_ints[0]}\nDay:{date_ints[1]}\nYear: {date_ints[-1]}')
print(f'Birthday\nMonth: {birth_ints[0]}\nDay:{birth_ints[1]}\nYear: {birth_ints[-1]} ')

if birth_ints[0] <= date_ints[0] and birth_ints[0] <= date_ints[0]:
    if age <= 0:
        age = 0
    print(f'You are {age} years old.')

elif (birth_ints[0] == date_ints[0]) and (birth_ints[1] == date_ints[1]):
    print(f'Happy Birthday!!\nYou are {age} now!!')

else:
    print(f'You are {age-1} years old.')
