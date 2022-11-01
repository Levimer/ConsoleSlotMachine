import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3


symbol_list = {
    'O': 5,
    'R': 5,
    'X': 3,
    'Y': 3,
    'Z': 1,

}

symbol_value = {
    'O': 2,
    'R': 2,
    'X': 5,
    'Y': 5,
    'Z': 10,

}


#  Function to generate a slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_list in symbols.items():  # loop through dictionary symbol
        for _ in range(symbol_list):  # add the symbol to all_symbols based on it's odds value
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # current symbols is a copy of all symbols
        for _ in range(rows):
            value = random.choice(current_symbols)  # random value from list
            current_symbols.remove(value)  # remove previous value from list
            column.append(value)  # add value to column list

        columns.append(column)

    return columns


# function to draw the slot machine
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:  # if i is not equal to the maximum index
                print(column[row], end=' | ')
            else:
                print(column[row], end='')

        print()


# Function to enter your deposit amount
def deposit():
    while True:
        amount = input('Enter your deposit amount: $')

        if amount.isdigit():
            amount = int(amount)  # Cast input into integer
            if amount > 0:
                break
            else:
                print("Deposit must be greater than 0.")
        else:
            print('Deposit must be a number')

    return amount


# Function to enter the amount of lines you want to gamble on
def get_lines_gamble():
    while True:
        gamble = input('Enter the amount of lines you want to bet on (1 - ' + str(MAX_LINES)+'): ')

        if gamble.isdigit():
            gamble = int(gamble)
            if 1 <= gamble <= MAX_LINES:  # if the input is in between the 0 and the maximum lines you can bet on
                break
            else:
                print("Must enter a value between 1 and "+str(MAX_LINES))
        else:
            print('Gamble amount must be a number')

    return gamble


# Function to enter the amount you would like to bet
def get_bet():
    while True:
        bet = input('Enter the amount you would like to bet: $ ')

        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:  # if the input is in between the min and max betting amounts
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}')
        else:
            print('Gamble amount must be a number')

    return bet


def game(balance):
    gamble = get_lines_gamble()

    while True:
        bet = get_bet()
        wager = bet * gamble
        if wager > balance:
            print(f'Insufficient initial capital, current balance: ${balance}')
        else:
            break

    print(f'You are betting ${bet} on a {gamble} line gamble. Total bet is equivalent to: ${wager}')

    slots = get_slot_machine_spin(ROWS, COLS, symbol_list)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, gamble, bet, symbol_value)
    print(f'You won ${winnings}')
    print(f'You won on lines:', *winning_lines)
    return winnings - wager


# function to check the amount of winnings
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break

        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def main():
    balance = deposit()
    while True:
        print(f'Current balance is ${balance}')
        spin = input('Press enter to play (q to quit)')
        if spin == 'q':
            break
        balance += game(balance)


main()
