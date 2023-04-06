# Tyfabian Williams
# 2142655

input_list = input().split()
list_of_int = [int(num) for num in input_list]


nun_neg_list = sorted([x for x in list_of_int if x >= 0])

for x in nun_neg_list:
    print(x, end=' ')
