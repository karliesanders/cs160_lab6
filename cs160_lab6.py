_author_ = 'Karlie Sanders'


def main():

    userInput = input("Enter a string: ")
    words = userInput.split()
    counts = {}
    for word in words:
        if word in counts.keys():
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1

    for key in sorted(counts.keys()):
        print("the word {0} occurs {1} times".format(key,counts[key]))

main()
