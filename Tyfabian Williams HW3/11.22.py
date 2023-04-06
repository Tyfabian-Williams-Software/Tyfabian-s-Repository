# Tyfabian Williams
# 2142655

user_input = input()
tokens = user_input.split()

for word in tokens:
    counter = tokens.count(word)
    print(word, counter)

