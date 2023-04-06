# Tyfabian Williams
# 2142655

def printRoster():
    keys = list(players.keys())
    keys.sort()
    print('ROSTER')
    for key in keys:
        print('Jersey number: %d, Rating: %d' %(key, players[key]))


players = {}

for i in range(5):
    jerseynum = int(input('Enter player %d\'s jersey number:\n' % (i+1)))
    players[jerseynum] = int(input('Enter player %d\'s rating:\n' % (i+1)))

    print()

    keys = list(players.keys())

    keys.sort()

print('ROSTER')
for key in keys:
    print('Jersey number: %d, Rating: %d' % (key, players[key]))

while True:
    print('\nMENU\n'
          'a - Add player\n'
          'd - Remove player\n'
          'u - Update player rating\n'
          'r - Output players above a rating\n'
          'o - Output roster\n'
          'q - Quit\n')
    choice = input('Choose an option:\n')

    if choice == 'a':
        jerseynum = int(input('Enter a new player\'s jersey number: \n'))
        newrating = int(input('Enter the player\'s rating:\n'))
        players[jerseynum] = newrating

    elif choice == 'd':
        jerseynum = int(input('Enter a player\'s jersey number: \n'))
        if jerseynum in list(players.keys()):
            del players[jerseynum]

    elif choice == 'u':
        jerseynum = int(input('Enter a player\'s jersey number: \n'))
        newrating = int(input('Enter a new rating for player:\n'))
        players[jerseynum] = newrating

    elif choice == 'r':
        newrating = int(input('Enter a rating:\n'))
        keys = list(players.keys())
        keys.sort()
        print('\nABOVE %d' %(newrating))
        count = 0
        for key in keys:
            if(players[key] > newrating):
                print('Jersey number: %d, Rating: %d' % (key, players[key]))
                count += 1
        if count == 0:
            print("No players found above %d rating" % (newrating))

    elif choice == 'o':
        printRoster()

    elif choice == 'q':
        break
