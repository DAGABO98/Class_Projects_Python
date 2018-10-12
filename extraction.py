def make_word_list(a_file):
    # Create a list of words from the file.
    word_list = []      # list of speech words: initialized to be empty

    for line_str in a_file:           # read file line by line
        line_list = line_str.split()  # split each line into a string
        for word in line_list:        # get words one at a time from list
            word = word.lower()       # make words lower case
            word = word.split(",")    # splits each string into a list of words
            if word != "--":
                word_list.append(word)   # add the word to the speech list

    a_file.close()

    return word_list


dictionary = make_word_list(open("dictionary.csv", "r"))


# this function opens the dictionary file and saves the changes line by line
def save_dictionary():
    f = open("dictionary-t.csv", "w")  # it is opening a dictionary-t, so dictionary.csv stays as a reference
    for l in dictionary:
        ll = ",".join(l)
        f.writelines(ll)
        f.write("\n")
    f.close()
