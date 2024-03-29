#Tyfabian Williams
#2142655
from datetime import date

#dictionary for the months with their number

months_dict = {
    'January': '1',
    'February': '2',
    'March': '3',
    'April': '4',
    'May': '5',
    'June': '6',
    'July': '7',
    'August': '8',
    'September': '9',
    'October': '10',
    'November': '11',
    'December': '12',
}
#modify to accept files and include an output file to write to


today = date.today().strftime('%#m/%#d/%Y')
token1 = today.split('/')
output_file = input()
input_file = input()

ofile = open(output_file, 'w')

with open(input_file, 'r') as file:
    for user_date in file:
        user_date = user_date.strip()
        if user_date == '-1':
            break

#using find to get if the format of the input is correct then extracting the date with condition

    month_index = user_date.find(' ')
    day_index = user_date[month_index + 1].find(', ')
    if month_index != '-1' and day_index != '-1':
        month = user_date[:month_index]
        day = user_date[month_index + 1:][:-day_index]
        year = user_date[-4:]
        month_num = months_dict[month]
        new_date = month_num + '/' + day + '/' + year + '\n'
        token2 = new_date.split('/')
        if (token1[0] >= token2[0] or token1[1] >= token2[1]) and token1[2] >= token2[2]:
            ofile.write(new_date)
