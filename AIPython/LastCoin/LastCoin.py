from random import randint
import sys


number_coins = int(input("How many coins on the table ? (20+) "))
user_starts = input("Do you want to start first ? (Yes/No) ")

def lastCoinGame(number_coins, user_starts):
    computer_take = computer_take_logic(number_coins)
    user_turn = True if user_starts.lower() == "yes" else False

    while number_coins > 0:
        if user_turn:
            user_desicion = int(input("How many coins do you want to take 1-3 ? "))
            number_coins -= user_desicion#
            if number_coins <= 0 :
                print(f"User took rest of the coins, User won!")
            else:
                print(f"User took {user_desicion} coins from table, there are {number_coins} coins left.")
            user_turn = False
        else:
            number_coins -= computer_take
            if number_coins <= 0:
                print(f"Computer took rest of coins, computer won!")
            else:
                print(f"Computer took {computer_take} coins from table, there are {number_coins} coins left.")

            user_turn = True
    


def computer_take_logic(how_many_table):
    if how_many_table >= 10:
        return randint(1,3)
    elif how_many_table <= 10:
        if how_many_table<= 3:
            return how_many_table
        elif how_many_table <= 7:
            return 1




print(lastCoinGame(number_coins, user_starts))