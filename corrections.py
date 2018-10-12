import extraction as ext
import string


correct_suggestions = []


# this function goes through the list of corrections and checks whether or not the words in it are part of the
# dictionary
def check_correction(result):
    for res in range(0, len(result)):  # loop for the words inside the list of corrections
        for l in range(0, len(ext.dictionary)):  # loop for the words inside the dictionary
            if result[res] == ext.dictionary[l][0]:
                correct_suggestions.append(result[res])  # appends corrections that are in the dictionary to a list


# this function transposes letters by dividing a word into independent character sequences that are then rearranged
def generate_transposes(word):
    result1 = []
    for letter in range(0, len(word)-1):
        char1 = word[:letter]
        char2 = word[letter]
        char3 = word[letter+1]
        char4 = word[letter+2:]
        n = char1 + char3 + char2 + char4
        result1.append(n)
    check_correction(result1)

    return result1


# this function loops through the indexes of a string, and then inserts a different character from a to z.
# the resulting word is then appended to a list, and the inserted character is deleted, so the process can be
# repeated
def insertion_letter(word1):
    result2 = []
    for i in range(0, len(word1)+1):
        list_word1 = list(word1)
        for n in range(0, 26):
            list_word1.insert(i, string.ascii_lowercase[n:n+1])
            word2 = "".join(list_word1)
            result2.append(word2)
            list_word1.pop(i)
    check_correction(result2)

    return result2


# this function creates a list of the characters in a string and then loops through the indexes, inserting
# a blank space. the resulting list is then converted in a pair of word, which are split and checked against
# the dictionary. If both words are in the dictionary, they are combined
# and appended to a list.
def insertion_space(word3):
    for i in range(1, len(word3)):
        list_word3 = list(word3)
        list_word3.insert(i, " ")
        word4 = "".join(list_word3)  # creates the string with the two words
        list_word3.pop(i)  # changes the list to the original arrangement before the blank space
        list_word4 = word4.split(" ")

        words = []

        for l in range(0, len(ext.dictionary)):  # checks whether the first word in in the dictionary
            if list_word4[0] == ext.dictionary[l][0]:
                words.append(list_word4[0])

        for l2 in range(0, len(ext.dictionary)):
            if list_word4[1] == ext.dictionary[l2][0]:  # checks whether the second word in in the dictionary
                words.append(list_word4[1])

        if len(words) == 2:  # joins the two words into a single string that is appended to the list of corrections
            new_words = " ".join(words)
            correct_suggestions.append(new_words)


# this function loops through the indexes for a string and deletes a single letter. the resulting word is checked
# against the dictionary. To restore the original string, the deleted character gets inserted into
# the list of characters.
def deletion(word5):
    result5 = []
    for i in range(0, len(word5)):
        list_word5 = list(word5)
        d = list_word5.pop(i)
        word6 = "".join(list_word5)
        result5.append(word6)
        list_word5.insert(i, d)
    check_correction(result5)

    return result5


# This function groups all the corrections together
def corrections(word7):
    generate_transposes(word7)
    insertion_letter(word7)
    insertion_space(word7)
    deletion(word7)