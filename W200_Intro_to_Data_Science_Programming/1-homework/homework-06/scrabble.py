# IMPORTS
import time

import score_word as sw

with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]

def mw(w, r):
    """Evaluates if a word in the pre-processed Scrabble dictionary can be constructed by the
        current rack. Iterates letter by letter through the word, evaluating if the remaining
        letters and wildcards are sufficient to construct it.
    """
    for i in w:
        if i in r:
            r = r.replace(str(i),"",1)
        elif "?" in r:
            r.replace("?","")
        elif "*" in r:
            r.replace("*","")
        else:
            return False

    return True


# User inputs their current Scrabble rack of 2 - 7 words without repeat letter limitations
# Includes input error-checking for rack length, non-alpha values, and excess wildcards

is_good = False
wild_card_count = 0
rack = ""
print("For this program, you will need to input a Scrabble rack. \nYour rack should be between"
      " 2 and 7 characters long and only include letters of the alphabet except for wildcards.\n"
      "Your rack may have up to 2 wildcards represented by * and ?")

keep_trying = True

while keep_trying:
    inp = input("Input a Scrabble Rack (ie. ABCDEFG):  ").lower()
    if len(inp) > 7 or len(inp) < 2:
        print("Invalid Input Length: Please input a rack between 2 and 7 characters")
    elif inp.count("?") > 1 or inp.count("*") > 1:
        print("Invalid Input: Rack must have no more than one of each wildcard")
    elif not inp.replace("?", "").replace("*", "").isalpha():
        print("Invalid Input: Rack must contain only letters and wildcards")
    else:
        rack = inp.lower()
        keep_trying = False

# The following code performs the following on each word in the Scrabble Dictionary
# (1) Eliminates word in the Scrabble Dictionary with a higher score than the total rack score
# (2) Eliminates word in the Scrabble Dictionary with a longer length than the total rack length
# (3) If the current word passes (1) and (2), runs score_word function to evaluate if it is possible
#     to construct the word with the current rack
# (4) Keeps track of the highest scoring word found so far.

start_time = time.time()
rack_score = sw.score_word(rack)
rack_length = len(rack)
clean_data = []
answers = []
highest = ['',0]

for i in data:
    i = i.lower()
    if len(i) <= rack_length and sw.score_word(i) < rack_score:
        clean_data.append(i)
        if mw(i,rack):
            # Run make_word reference
            answers.append((sw.score_word(i),i))
            if sw.score_word(i) > highest[1]:
                highest = [i, sw.score_word(i)]

# Formatted printing of the number of possible words, the list of possible words, and the highest point value
#Sort alphabetically and by score
print("Rack Score:", rack_score)
print("Length of clean data: ", len(clean_data))
print("Total Number of Words:",len(answers))
for i in sorted(answers,reverse=True):
    print(i)
print("Highest:", highest)
print("Run Time: ",time.time()-start_time,"s")




