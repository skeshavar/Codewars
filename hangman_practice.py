import random

listOfWords = ("hangman", "chairs", "backpack", "bodywash", "clothing", "computer", "python", "program", "glasses", "sweatshirt", "sweatpants", "mattress", "friends", "clocks", "biology", "algebra", "suitcase", "knives", "ninjas", "shampoo")
randomNumber = random.randint(0, len(listOfWords) - 1)
guess = listOfWords[randomNumber]
guess_list = list(guess);
answer = [];
wrong_guess = [];
theBoard=[];
rightans = "";
count1 = 7;
for i in guess:
    theBoard.append("*")
while count1 > 0:
    m = raw_input ("What is the letter")
    count_rep = guess.count(m);
    
    if m in guess and m in answer:
        print "Oops! Already guessed"
        print theBoard
    if m in wrong_guess:
        print "Oops! Already guessed"
        print theBoard
    if m in guess and m not in answer:
        if count_rep >= 2:
            answer1 = [x for x,y in enumerate(guess) if y == m]
            for i in range(len(answer1)):
                theBoard[answer1[i]] = m
            for i in range(count_rep):
                answer.append(m)
        else:
            guess_letter = guess.index(m)
            theBoard[guess_letter] = m
            answer.append(m)
        print theBoard
    if m not in guess:
        print "Wrong! Guess again"
        count1 -= 1;
        wrong_guess.append(m)
        print theBoard
        
    if len(guess)==len(answer):
        print guess
        print "Yes! You have won the game ! Congratulations!!!"
        break
        
    if count1 == 6:
		    print "________      "
		    print "|      |      "
		    print "|             "
		    print "|             "
		    print "|             "
		    print "|             "
    elif count1 == 5:
		    print "________      "
		    print "|      |      "
		    print "|      0      "
		    print "|             "
		    print "|             "
		    print "|             "
    elif count1 == 4:
	    	print "________      "
	    	print "|      |      "
	    	print "|      0      "
	    	print "|     /       "
	    	print "|             "
	    	print "|             "
    elif count1 == 3:
		    print "________      "
		    print "|      |      "
		    print "|      0      "
		    print "|     /|      "
		    print "|             "
		    print "|             "
    elif count1 == 2:
            print "|             "
            print "|      |      "
            print "|      0      "
            print "|     /|\     "
            print "|             "
            print "|             "
    elif count1 == 1:
            print "|             "
            print "|      |      "
            print "|      0      "
            print "|     /|\     "
            print "|     /       "
            print "|             "
    elif count1 == 0:
            print "|             "
            print "|      |      "
            print "|      0      "
            print "|     /|\     "
            print "|     / \     "
            print "|             "
            print "Game Over! You lost the game!"
            print "The right answer is " + guess