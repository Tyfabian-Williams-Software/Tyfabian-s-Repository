#Tyfabian Williams
#2142655


word = input()
new_word = ''.join(word.split())
palindrome = new_word[::-1]
if new_word == palindrome:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')
    