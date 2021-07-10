import random
import csv


def error1():
    print("  O  ")

def error2():
    print("  O  ")
    print("  |  ")
    print("  |   ")

def error3():
    print("   O   ")
    print("  \\|   ")
    print("   |    ")

def error4():
    print("   O    ")
    print("  \\|/   ")
    print("   |    ")

def error5():
    print("   O    ")
    print("  \\|/   ")
    print("   |    ")
    print("  /     ")

def error6():
    print("   O    ")
    print("  \\|/   ")
    print("   |    ")
    print("  / \\   ")


with open("Hangman_wordbank.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for word in csv_reader:
        question = word
csv_file.close()
guess = []
tries = 6
stored = ""
check = True
n = random.randint(0, len(question) - 1)
# question[n] = question[n][1:]  # This is to remove the extra space from the left side of word
question[n] = question[n].lstrip()  # This is to remove the extra space from the left side of word
question_length = len(question[n])
for i in range(question_length):
    stored = stored + "_ "
print(stored)

while check and tries != 0:
    if tries == 5:
        error1()
    elif tries == 4:
        error2()
    elif tries == 3:
        error3()
    elif tries == 2:
        error4()
    elif tries == 1:
        error5()
    c = 0
    letter = input("\nEnter a letter: ")
    if letter in guess:
        print("\nYou have already used this letter.\n")
        print("\nstored")
        continue
    else:
        guess.append(letter)
    check = False
    if letter in question[n]:
        for i in stored:
            if i == " ":
                stored = stored + " "
                c -= 1
            elif i != "_":
                stored = stored + i
            elif question[n][c] == letter:
                stored = stored + letter
            else:
                stored = stored + "_"
                check = True
            c += 1
        stored = stored[question_length * 2:]  # To remove the previous string from stored variable
        print("\n" + stored + "\n")
    else:
        tries -= 1
        print("\nYou have {} chances remaining".format(tries))
        print("\n" + stored + "\n")
        check = True

if not check:
    print("\n\nYou have won the game")
else:
    error6()
    print("\n\nYou have lost")
    print("\nThe word was {}".format(question[n]))


