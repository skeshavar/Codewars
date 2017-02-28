guess = "keshava";
guess_list = list(guess);
answer = [];
rightans = "";
count1 = 7;
while count1 > 0:
    m = raw_input ("What is the letter")
    count_rep = guess.count(m);
    
    if m in guess and m in answer:
        print "Oops! Already guessed"
        
    if m in guess and m not in answer:
        if count_rep >= 2:
            for i in range(count_rep):
                answer.append(m)
        else:
            answer.append(m)
        
    if m not in guess:
        print "Wrong! Guess again"
        count1 -= 1;
        
    if len(guess)==len(answer):
        print guess
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
    