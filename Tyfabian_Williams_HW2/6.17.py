#Tyfabian Williams
#2142655

password = input()


def password_enhancer(pw):
    pw = pw.replace("i", '!')
    pw = pw.replace("a", '@')
    pw = pw.replace("m", 'M')
    pw = pw.replace("B", '8')
    pw = pw.replace("o", '.')
    pw = pw + 'q*s'
    return pw


print(password_enhancer(password))
