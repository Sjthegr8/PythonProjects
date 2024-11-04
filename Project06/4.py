import string
from operator import itemgetter


def add_word(word_map, word):
    """
    adds word to the word_mao
    :param word_map:
    :param word:
    :return:
    """
    # add word to word_map if it not preent
    if word not in word_map:
        word_map[word] = 1
    else:
    # if present incerement the count
        word_map[word] += 1


def build_map(in_file, word_map):
    """

    :param in_file:
    :param word_map:
    :return:
    """
    for line in in_file:

        # split each of the word of each of the lines of the file and make a list of words
        word_list = line.split()

        for word in word_list:
            # extract each words from the list by removing white spaces
            word = word.strip().strip(string.punctuation).lower()
            if word != "":
                add_word(word_map, word)


def display_map(word_map):
    """

    :param word_map:
    :return:
    """
    # sort dict based on frequency
    sorted_list_alpha = sorted(word_map.items(),key = itemgetter(0))
    freq_list = sorted(sorted_list_alpha, key=itemgetter(1), reverse = True)

    print("\n{:15s}{:5s}".format("Word", "Count"))
    print("-" * 20)
    for item in freq_list:
        print("{:15s}{:>5d}".format(item[0], item[1]))


def open_file():
    """
    opening the file
    :return: fp(file pointer)
    """
    file_exists = False

    while not file_exists:
        try:
            file_name = input(":~Enter file name ~:")
            fp = open(file_name, "r")
            return fp

        except FileNotFoundError:
            print("\n*** unable to open file ***\n")


def main():
    """
    creates a dictionary, calling all functions
    :return:
    """
    word_map = {}
    in_file = open_file()
    print()
    build_map(in_file, word_map)
    display_map(word_map)
    in_file.close()


if __name__ == "__main__":
    main()
