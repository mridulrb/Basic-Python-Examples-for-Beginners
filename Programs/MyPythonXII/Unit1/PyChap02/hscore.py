# File name: ...\\MyPythonXII\Unit1\PyChap02\hscore.py
# Menu drive program to list players scores, input scores, and find total scores.
# Also print the total score while listing the scores.
scores = []
choice = None
while choice != "0":
    print ("High Scores Keeper")
    print ("0 - Quit")
    print ("1 - Add a Score")
    print ("2 - List Scores\n")
    choice = input("Choice: ")
    print()
    # exit
    if choice == "0":
        print ("Good-bye.")
    # add a score
    elif choice == "1":
        name = input("What is the player's name?: ")
        score = int(input("What score did the player get?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort()
        scores.reverse() # want the highest number first        
    # display high-score table
    elif choice == "2":
        tscore = 0
        if len(scores) > 0:
            print ("NAME\t\tSCORE")
            for entry in scores:
                score, name = entry
                tscore = tscore + score
                print (name, "\t\t", score)
            print ("Total score is:", tscore)
            print()
        else:
            print ("The list is empty")
            print ("Please try option 2.")
        
    # some unknown choice
    else:
        print ("Sorry, but", choice, "isn't a valid choice.")
        
        
    
