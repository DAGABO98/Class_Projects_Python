import checking_functions as cf
import extraction


def main2():
    done = False

    while not done:
        w = input("Please enter a word (enter -1 to end: ")
        if w == "-1":
            print("Exiting.")
            break

        c = cf.check_word(w)


        if c == True:
            print("The word is correctly spelled.")
        elif c == False:
            print("Invalid output")
        else:
            print("Suggested corrections are: ", c)
            f = input("Enter one of the words or your own correction: ")
            cf.update_corrections(w, f)
        extraction.save_dictionary()


main2()
