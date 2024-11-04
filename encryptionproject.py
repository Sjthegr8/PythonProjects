################################################################################
#
# Computer Project 03
#
# The following python script uses the method of encryption and de-encryption in
# which a message is encrypted and can be de-encrypted for saving the Tatooine planet
#
# Description-:
#
#     1. The banner is displayed and menu appears from which an option can be selected
#     2. Either you can decompress or encrypt a message
#     3. the encryption is done into gibberish and each and every step is checked
#     4. You can exit the program after your process is complete
#
################################################################################


banner = '''
    .    .         .      .             . .     .        .          .          .
        .                 .                    .                .
    .               A long time ago in a galaxy far, far away...   .
        .      .   A terrible civil war burns throughout the  .        .     .
            .     galaxy: a rag-tag group of freedom fighters   .  .
    . .       .  has risen from beneath the dark shadow of the            .
.        .     evil monster the Galactic Empire has become.                  .  .
    .      Outnumbered and outgunned,  the Rebellion burns across the   .    .
.      vast reaches of space and a thousand-thousand worlds, with only     .
    . their great courage - and the mystical power known as the Force -
    flaming a fire of hope.                                   .

        ~~ Your mission: Tatooine planet is under attack from stormtroopers,
            and there is only one line of defense remaining        
        It is up to you to stop the invasion and save the planet~~    

'''

menu = '''\nPlease choose one of the options below:
\tD. Decompress a message.
\tE. Encrypt a message.
\tH. Display the menu of options.
\tX. Exit.'''

open = '('
close = ')'
comma = ','
backslash = '\\'
newline = '\n'
vowels = "aeiouAEIOU"

print(banner)
print(menu)


"Invalid options. Please try again"
"Exiting program...\nMay the force be with you!"
"\n:~Enter option ~:"

"The string should not be empty. Please try again"
"\nThe decompressed string prints as:"
"\n:~Enter a non-empty string to decompress ~:"

"\nEnglish to Gibberish translator"
"\n:~Enter your first Gibberish syllable (add * for the vowel substitute) ~:"
"\nYour final sentence:"
"\n:~Please enter a sentence you want to translate ~: \n---> "
"Syllable must only contain letters or a wildcard ('*')"
"\n:~Enter the second Gibberish syllable (* for vowel substitute) ~:"



while True:
    menu_input = str(input("\n:~Enter option ~:"))
    if menu_input == "":
        print("Invalid options. Please try again")
        print(menu)
        continue
    if menu_input == 'D' or menu_input == 'd':
        while True:
            user_input = input("\n:~Enter a non-empty string to decompress ~:")
            if user_input == '':
                print("The string should not be empty. Please try again")
                continue
            if user_input != '':
                i = 0
                while open in user_input:
                    open_find = user_input.find(open)
                    comma_find = user_input.find(comma, open_find)
                    close_find = user_input.find(close, comma_find)
                    front = int(user_input[open_find + 1:comma_find])
                    back = int(user_input[comma_find + 1: close_find])
                    y = user_input[0:open_find] + user_input[open_find - front: open_find - front + back] + user_input[close_find + 1:]
                    user_input = y
                    i += 1
                y = user_input.replace(backslash, '\n')
                print("\nThe decompressed string prints as:")
                print(y)
                break
    elif menu_input == 'E' or menu_input == 'e':
        print("\nEnglish to Gibberish translator")
        while True:
            while True:
                first = input("\n:~Enter your first Gibberish syllable (add * for the vowel substitute) ~:")
                if first.isalpha() == False:
                    if '*' in first:
                        break
                    print("Syllable must only contain letters or a wildcard ('*')")
                    continue
                else:
                    break
            while True:
                second = input("\n:~Enter the second Gibberish syllable (* for vowel substitute) ~:")
                if second.isalpha() == False:
                    if '*' in second:
                        break
                    print("Syllable must only contain letters or a wildcard ('*')")
                    continue
                else:
                    break
            user_input = input("\n:~Please enter a sentence you want to translate ~: \n---> ")
            for t, x in enumerate(user_input):
                if x in vowels:
                    break
            value = False
            random = ""
            i = 0
            while i < len(user_input):
                char = user_input[i]
                if char in vowels and user_input[i - 1] not in vowels:
                    if value == False:
                        if '*' in first:
                            first = first.replace('*', char)
                            random += first + char
                        else:
                            random += first + char
                        value = True
                    else:
                        if '*' in second:
                            second_temp = second.replace('*', char)
                            random += second_temp + char
                        else:
                            random += second + char
                else:
                    random += char
                i += 1
            print("\nYour final sentence:")
            print(random)
            break
    elif menu_input == 'H' or menu_input == 'h' :
        print(menu)
        continue
    elif menu_input == 'X' or menu_input == 'x':
        print("Exiting program...\nMay the force be with you!")
        exit()
    else:
        print("Invalid options. Please try again")
        print(menu)



