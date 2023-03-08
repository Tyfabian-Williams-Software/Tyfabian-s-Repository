#Tyfabian Williams
#2142655

def exact_change(user_total):
    nd = user_total // 100
    nq = user_total % 100 // 25
    ndi = user_total % 100 % 25 // 10
    nn = user_total % 100 % 25 % 10 // 5
    np = user_total % 100 % 25 % 10 % 5 // 1
    return nd, nq, ndi, nn, np


if __name__ == '__main__':

    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if num_dollars != 0:
        if num_dollars == 1:
            print(num_dollars, 'dollar')
        else:
            print(num_dollars, 'dollars')

    if num_quarters != 0:
        if num_quarters == 1:
            print(num_quarters, 'quarter')
        else:
            print(num_quarters, 'quarters')

    if num_dimes != 0:
        if num_dimes == 1:
            print(num_dimes, 'dime')
        else:
            print(num_dimes, 'dimes')

    if num_nickels != 0:
        if num_nickels == 1:
            print(num_nickels, 'nickel')
        else:
            print(num_nickels, 'nickels')

    if num_pennies != 0:
        if num_pennies == 1:
            print(num_pennies, 'penny')
        else:
            print(num_pennies, 'pennies')
    if input_val == 0:
        print('no change')
