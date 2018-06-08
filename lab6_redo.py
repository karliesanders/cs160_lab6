_author_ = 'Karlie Sanders'


def file_reader():
    user_file = input("enter file name: ")
    with open('lab6file.txt') as file:
        whole_file_as_string = file.read().replace('\n', ' ')
    print(whole_file_as_string)
    file.close()
    return(whole_file_as_string)

def word_counter():
    words = file_reader().split()
    counts = {}
    for word in words:
        if word in counts.keys():
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1

    for key in sorted(counts.keys()):
        print("the word {0} occurs {1} times".format(key, counts[key]))

word_counter()

