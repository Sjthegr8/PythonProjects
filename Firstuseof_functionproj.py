################################################################################
#
# Computer Project 04
# Defines commands as functions
# Defines the left current and right brackets and prints the menu
# Asks the user for an input
# Performs function matching input by user
# prints the current line and menu
# asks for another input
#
################################################################################
def hint(user):
    """
    :param user:
    :return:
    """
    print(user)

def load(user,a,b,c):
    """

    :param user:
    :param a:
    :param b:
    :param c:
    :return:
    """

    a = ""
    find_space = user.find(" ")
    if find_space == -1:
        b = b + user
        return "",b,""
    else:
        b = user[:find_space]
        c = user[find_space + 1:]
        return a,b,c

def next(a,b,c):
    """
[ ]
    :param a:
    :param b:
    :param c:
    :return:
    """
    if c != "":
        if a == "":
            a = a+b
        else:
            a = a + " " + b
        find_space = c.find(" ")
        if find_space == -1:
            b = c[0:]
            c = ""
        else:
            b = c[0:find_space]
            c = c[find_space+1:]
    else:
        print("Reached end of string.")
    c = c.strip()
    return a,b,c

def prev(a,b,c):
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    if a != '':
        if a == "":
            c = b
        else:
            c = b + " " + c
        space = a.rfind(" ")
        if space == -1:
            b = a
            a = ""
        else:
            b = a[space + 1:]
            a = a[0:space]
    else:
        print("Reached beginning of string.")
    c = c.strip()
    return a,b,c

def replace(u,a,b,c):
    """

    :param u:
    :param a:
    :param b:
    :param c:
    :return:
    """
    b = u
    return u,a,b,c

def insert(u,a,b,c):
    """

    :param u:
    :param a:
    :param b:
    :param c:
    :return:
    """
    if a == "":
        a = u
    else:
        a = a + " " + u
    return u,a,b,c

def erase(a,b,c):
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    b = ""
    if a=="" and c=="":
        return a, b, c
    if c == "":
        a,b,c = prev(a,b,c)
    else :
        a,b,c = next(a,b,c)
    a = a.strip()
    return a,b,c

def copy(user,a,b,c):
    """

    :param user:
    :param a:
    :param b:
    :param c:
    :return:
    """
    if b == "":
        print("No word in buffer.")
    else:
        user = b
        b = ""
        if c !="":
            a,b,c = next(a,b,c)
        else:
            a,b,c = prev(a,b,c)
        a= a.strip()
        return user,a,b,c

def cut(user,a,b,c):
    """

    :param user:
    :param a:
    :param b:
    :param c:
    :return:
    """
    user,a,b,c = insert(user,a,b,c)
    a = a.strip()
    user = ""
    return user,a,b,c

def main():
    banner = """
    Welcome to the Ancient Scroll Text Editor!
    Use hidden commands to control the words in the text,
    but beware, There is no cursor to guide you—only your imagination!
    """

    menu = '''\n--------------------------------------
    Commands available:
        'n': Move to the Next word
        'p': Retreat to the Previous word
        'i': Insert a new word 
        'e': Erase the current word as if it never existed
        'r': Replace the current word with one of your choosing
        'c': Cut the word and trap it in the buffer
        'v': Copy a word from buffer to place before the current word
        'l': Load a new string of text
        'h': Reveal the hidden commands (Help)
    --------------------------------------
    '''
    buffer = ""
    first = ''
    current = ''
    rest = ''
    line = "[ {} ] [ {} ] [ {} ]".format(first, current, rest)
    print(banner)
    while True:
        print("\nCurrent line:")
        print(line)
        print(menu)
        comm = input(":~Enter a command (q to quit) ~:")
        comm = comm.lower()
        if comm == "n":
            line = "[ {} ] [ {} ] [ {} ]"
            first,current,rest = next(first,current,rest)
            line = line.format(first, current, rest)
        elif comm == "l":
            line = "[ {} ] [ {} ] [ {} ]"
            user_input = input(":~Input a string ~:")
            first,current,rest = load(user_input,first,current,rest)
            line = line.format(first, current, rest)
        elif comm == "p":
            line = "[ {} ] [ {} ] [ {} ]"
            first,current,rest = prev(first,current,rest)
            line = line.format(first, current, rest)
        elif comm == "r":
            line = "[ {} ] [ {} ] [ {} ]"
            while True:
                user= input(":~Enter word to replace current word ~:")
                user.strip()
                x = user.find(' ')

                if x == -1 and user != '':
                    user, first, current, rest = replace(user, first, current, rest)
                    line = line.format(first, current, rest)
                    break
                else:
                    print("Please enter a single word (no spaces, non-empty string).")



        elif comm == "i":
            line = "[ {} ] [ {} ] [ {} ]"
            while True:
                user= input(":~Enter word to insert before current word ~:")
                if user.isalpha():
                    user,first,current,rest = insert(user,first,current,rest)
                    line = line.format(first, current, rest)
                    break
                else:
                    print("Please enter a single word (no spaces, non-empty string).")
        elif comm == "e":
            line = "[ {} ] [ {} ] [ {} ]"
            first, current, rest = erase( first, current, rest)
            line = line.format(first, current, rest)
        elif comm == "h":
            hint(menu)
        elif comm == "q":
            print("Program completed.")
            break
        elif comm == "c":
            line = "[ {} ] [ {} ] [ {} ]"
            buffer=""
            buffer,first, current, rest = copy(buffer,first, current, rest)

            line = line.format(first, current, rest)
        elif comm == "v":
            if buffer == "":
                print("No word in buffer.")
            else:
                line = "[ {} ] [ {} ] [ {} ]"
                buffer, first, current, rest = cut(buffer, first, current, rest)

                line = line.format(first, current, rest)
        else:
            print("Invalid Command.")
# DO NOT MODIFY THE FOLLOWING 2 LINES.
# DO NOT WRITE ANYTHING AFTER THE FOLLOWING 2 LINES OF CODES
# All your code should be either in the main function
# or in a function.
if __name__ == "__main__":
    main()


