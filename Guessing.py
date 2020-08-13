print("Guess any number between 0-50:\n")

secret_number = 44
Guess_number = ''
count = 0
limit = 3
out_of_moves = False

while Guess_number != secret_number and not(out_of_moves):
    if count < limit:
        Guess_number = int(input("Enter guess: "))
        count += 1
    else:
        out_of_moves = True
if out_of_moves:
    print("Out of moves, You lost!")
else:
    print("You win !")
