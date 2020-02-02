############### An Introduction to Python ###############
####################### Homework 2 ######################

### GAME INSTRUCTION FOR CODE ###

# The player is trapped in the “magic maze”.
# If still in the “magical maze”, ask the player which way to go. Announce it like:“You are in the magic maze. Which way to go? (N,S,E,W)”
# Accepted directions are N[orth], S[outh], E[ast] and W[est].
# The secret escape combination is: SSNWES
# Keep track of the number of “moves”
# If the escape sequence is correct, announce that the player has won:“You have escaped the maze in X moves”
# If the escape chain is broken, start from the beginning. Suppose the player has the sequence SSN and then tries E. This breaks the chain an we must start again from the first valid move: S.
# After 5 moves the player loses one life
# The player starts with 3 lives and “dies” when the life counter reaches 0
# Inform the player when he loses one life and how many he has left
# Try not to use something that we have not learned yet.

moves = 0
wrong_moves_counter = 0
life_counter = 0
secret_key = 1

while True:

    while life_counter < 3:

        while wrong_moves_counter < 5:

            if secret_key == 1:

                move1 = input("You are in the magic maze. Which way to go? (N,S,E,W)")
                print("You entered:", move1)

                if move1 == "S" or move1 == "s":
                    print("You have found secret key number", secret_key)
                    secret_key += 1
                    moves += 1


                else:
                    wrong_moves_counter += 1
                    secret_key = 1
                    moves += 1
                    print("Your input is wrong, please try again. You have", wrong_moves_counter,
                          "Wrong move, you are allowed 5")
                    break

            if secret_key == 2:

                move2 = input(" Which way to go next? (N,S,E,W)")
                print("You entered:", move2)

                if move2 == "S" or move2 == "s":
                    print("You have found secret key number", secret_key)
                    secret_key += 1
                    moves += 1


                else:
                    wrong_moves_counter += 1
                    secret_key = 1
                    moves += 1
                    print("Your input is wrong, please try again. You have", wrong_moves_counter,
                          "Wrong move, you are allowed 5")
                    break

            if secret_key == 3:

                move3 = input(" Which way to go next? (N,S,E,W)")
                print("You entered:", move3)

                if move3 == "N" or move3 == "n":
                    print("You have found secret key number", secret_key)
                    secret_key += 1
                    moves += 1


                else:
                    wrong_moves_counter += 1
                    secret_key = 1
                    moves += 1
                    print("Your input is wrong, please try again. You have", wrong_moves_counter,
                          "Wrong move, you are allowed 5")
                    break

            if secret_key == 4:

                move4 = input(" Which way to go next? (N,S,E,W)")
                print("You entered:", move4)

                if move4 == "W" or move4 == "w":
                    print("You have found secret key number", secret_key)
                    secret_key += 1
                    moves += 1


                else:
                    wrong_moves_counter += 1
                    secret_key = 1
                    moves += 1
                    print("Your input is wrong, please try again. You have", wrong_moves_counter,
                          "Wrong move, you are allowed 5")
                    break

            if secret_key == 5:

                move5 = input(" Which way to go next? (N,S,E,W)")
                print("You entered:", move5)

                if move5 == "E" or move5 == "e":
                    print("You have found secret key number", secret_key)
                    secret_key += 1
                    moves += 1


                else:
                    wrong_moves_counter += 1
                    secret_key = 1
                    moves += 1
                    print("Your input is wrong, please try again. You have", wrong_moves_counter,
                          "Wrong move, you are allowed 5")
                    break

            if secret_key == 6:

                move6 = input(" Which way to go next? (N,S,E,W)")
                print("You entered:", move6)

                if move6 == "S" or move6 == "s":
                    secret_key += 1
                    moves += 1
                    print("Congratulations, You have escaped the maze in ", moves, "moves!!!")


                else:
                    wrong_moves_counter += 1
                    secret_key = 1
                    moves += 1
                    print("Your input is wrong, please try again. You have", wrong_moves_counter,
                          "Wrong move, you are allowed 5")
                    break

        if wrong_moves_counter >= 5:
            life_counter += 1
            wrong_moves_counter = 0
            moves += 1
            print("You lost one life, you have", 3- life_counter, "lives left")

    if life_counter >= 3:
        print("GAME OVER, you lost!")
        break