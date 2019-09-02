#!/usr/bin/python3
import urllib.request
import random



def is_word_line(line):
    line = line.strip()
    if len(line) <= 0: return False

    return (line == line.upper()) and (line[0] not in ["(", "*", "-"]) and (line[-1] not in ["-", ".", ")"])

def main():
    print()
    print("Downloading The Project Gutenberg EBook of Webster's Unabridged Dictionary from https://www.gutenberg.org/ebooks/29765.txt.utf-8")
    dictionary = urllib.request.urlopen("https://www.gutenberg.org/ebooks/29765.txt.utf-8").read().decode("utf-8").split("\n")
    #dictionary = open("websters_unabridged.txt").readlines()

    words = {line.strip() for line in dictionary if is_word_line(line)}
    word_count = len(words)
    
    print("total words={}".format(word_count))
    
    print("How many words should be viewed?")
    num_guesses = int(input(" > "))
    
    known_word_count = 0
    for (word, index) in [(random.choice(tuple(words)), i) for i in range(1,num_guesses+1)]:
        print("[{}/{}] Do you know the word \"{}\"? (Enter 'y' or 'n')".format(index, num_guesses, word))
        reply = ""
        while reply.lower() not in ["y", "n"]:
            reply = input(" > ")
        if reply == "y":
            known_word_count += 1
    
    percent_known = float(known_word_count) / num_guesses
    words_known_estimate = word_count * percent_known
    
    print()
    print("==Final Stats==")
    print("Total words found in dictionary: {}".format(len(words)))
    print("Total words viewed: {}".format(num_guesses))
    print("Number of words known: {}".format(known_word_count))
    print("Percent of words known: {}%".format(percent_known*100))
    print()
    print("**It seems like you know roughly {} of these words**".format(words_known_estimate))
    print()

main()

