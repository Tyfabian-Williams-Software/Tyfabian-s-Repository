#Tyfabian Williams
#2142655

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    # FIXME: The following line will throw ValueError exception.
    #        Insert try/except blocks to catch the exception.
    try:
        age = int(parts[1]) + 1
        print(f'{name} {age}')

    except ValueError:
        print("{} {}".format(name, 0))

    # Get next line
    parts = input().split()
    name = parts[0]
