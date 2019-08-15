import random 
import csv
import time
import sys

#create list of words for games
words = []
with open('words.csv', 'rb') as csvFile:
        wordfile = csv.DictReader(csvFile)
        for row in wordfile:
            word = row["#words"]
            words.append(word)           

moreWords = []
txt = open('words.txt', 'r').read().splitlines()
for line in txt:
    moreWords.append(line)
    
#function to print out phrases one letter at a time on the same line            
def say(phrase):
    out = ""
    for p in phrase:
        out = out + p
        sys.stdout.write("\r" + str(out))
        sys.stdout.flush()
        time.sleep(0.03)
    print("")

#word chain game
def wordchain():
    play = True
    while play:

        #construct word chain
        chain = []
        random.shuffle(moreWords)
        currentWord = random.choice(moreWords)
        chain.append(currentWord)
        for word in moreWords:
            count = 0
            if len(word) == len(currentWord):
                for i in range(len(currentWord)):
                    if word[i] != currentWord[i]:
                        count = count + 1
                if count == 1 and word not in chain:
                    chain.append(word)
                    currentWord = word
                    
        if len(chain) == 5:

            #construct answer list
            answer = []
            blank = ""
            for i in range(len(currentWord)):
                blank = blank + '-'
            answer.append(chain[0])
            for i in range(1,4):
                answer.append(blank)
            answer.append(chain[4])
            
            #gameplay
            guessing = True
            say("Welcome to Word Chain. Each word is different by one letter.")
            say("Guess words to complete the chain. Type 'give up' to see the solution.")
            print("")
            while guessing:
                for i in answer:
                    print i
                print("")
                guess = raw_input()
                if guess == 'give up':
                    guessing = False
                    say("Hard luck! The solution was:")
                    for i in chain:
                        print i        
                elif guess not in chain:
                    say("...Nope")
                    print("")
                else:
                    say("...Correct!")
                    print("")
                    for i in range(len(answer)):
                        if guess == chain[i]:
                            answer[i] = chain[i]
                    if answer == chain:
                        guessing = False
                        say("Congrats you win!")
                        for i in answer:
                            print i
            again = raw_input("Play again? y or n. \n")
            if again == 'n':
                play = False
                    

#hangman game
def hangman():
    solved = False
    play = True
    used = []
    chances = 10
    answer = random.choice(words)
    word = ""
    for i in range(len(answer)):
        word = word + "_"


    say("Welcome to hangman!")
    while play:
        say("Guess a letter")
        while not solved and chances > 0:
            left = "Chances left: %s" % str(chances)
            say(left)
            #print("Previous guesses: " + str(used))
            letters = "%s letters:" % str(len(answer))
            say(letters)
            say(word)
            guess = raw_input()
            if guess.lower() in used:
                say("You already used that letter.")
            elif guess.lower() not in answer:
                chances = chances - 1
                say("...Nope!")
                used.append(guess)
            elif guess.lower() in answer:
                for i, letter in enumerate(answer):
                    if guess.lower() == letter:
                        word = word[:i] + guess + word[i+1:]
                used.append(guess)
                say("...Correct!")
                if word == answer:
                    solved = True
        if solved:
            end = "The answer was: %s" % str(answer)  
            say("Congratulations. You win!")
            say(end)
        else: 
            say("Game over. You lose!")
            end = "The answer was: %s" % str(answer)
            say(end)
        again = raw_input("Play again? y or n. \n")
        if again == 'n':
            play = False
        else:
            answer = random.choice(words)
            solved = False
            used = []
            word = ""
            for i in range(len(answer)):
                word = word + "_"
            chances = 10
                


    
#a simple guess the number game
def guess():
    num = random.randint(1,10)
    solved = False
    play = True
    while play:
        say("Guess a number between 1 and 10\n")
        while not solved:       
            guess = input()
            if guess == num:
                say("Correct! You win.")
                solved = True
            else:
                say("Wrong. Try again")
        again = raw_input("Guess again? y or n. \n")
        if again == 'n':
            play = False
        else:
            num = random.randint(1,10)
            solved = False
          
#play script         
say("Welcome to Beany Games!")
playing = True

while playing:
    say("Type a number to choose a game:(1)Guess (2)Hangman (3)Word Chain or (0)Quit")
    game = input()
    if game == 1:
        guess()
    elif game == 2:
        hangman()
    elif game == 3:
        wordchain()
    elif game == 0:
        say("Thanks for playing, bye!")
        playing = False
    
    



                    








    









