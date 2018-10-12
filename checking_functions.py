import extraction as ext
import corrections as cr
import copy


# this function checks if a word is in the dictionary. If it is, the function returns a success message and a True
# value. If it is not, the function calls to the four correction functions to generate a list of potential spellings.
# It also checks whether or not a common correction to a misspelling has already been selected.
def check_word(word):
    try:
        for i in range(0, len(ext.dictionary)):
            if word == ext.dictionary[i][0]:  # checks if the word is in the dictionary
                print("success")
                return True
            elif word == "" or word == " ":
                raise TypeError
            if len(ext.dictionary[i]) >= 8 and ext.dictionary[i][0] != "the":
                for position in range(1, len(ext.dictionary[i])):
                    if word in ext.dictionary[i][position]:  # checks if the user has previously selected a correction
                        print("previous correction", (ext.dictionary[i][0]))
            if len(ext.dictionary[i]) >= 9 and ext.dictionary[i][0] == "the":
                for position in range(1, len(ext.dictionary[i])):
                    if word in ext.dictionary[i][position]:  # checks if the user has previously selected a correction
                        print("previous correction", (ext.dictionary[i][0]))
        cr.corrections(word)
        suggestions = copy.deepcopy(cr.correct_suggestions)
        del cr.correct_suggestions[:]
        return suggestions
    except TypeError:
        print("Please enter a valid input")
        return False


# this function updates the times_selected_value for each of the corrections selected. it also appends the misspelled
# word so that it can be linked with the corrected word and return as a previous correction
def update_corrections(original_word, corrected_word):
    done = False
    for i in range(0, len(ext.dictionary) - 1):
        if corrected_word == ext.dictionary[i][0]:
            done = True
            ext.dictionary[i][3] = int(ext.dictionary[i][3]) + 1
            ext.dictionary[i][3] = str(ext.dictionary[i][3])
            if ext.dictionary[i][len(ext.dictionary[i]) - 1] != original_word:
                ext.dictionary[i].append(original_word)
            del cr.correct_suggestions[:]
    if not done:
        ext.dictionary.append([corrected_word, "", "user created", "1", "", original_word])
