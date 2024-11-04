#######################################################################################################################
#
# Computer Project 06
#
#######################################################################################################################

import csv
from operator import itemgetter

# Lists of valid personalities and games


# Use these in your input statement
"\n:~Enter the Species ID file ~:"
"\n:~Enter the Expenses file ~:"
"\n:~Enter the number of Zoo files available (at least two) ~:"
"\n:~Enter a Zoo name ~:"
"\n:~Input a choice ~:"

":~Enter a zoo ~:"
":~Enter an animal species ~:"
":~Enter the animal’s name ~:"


# Use these in your print statement
"Error. File does not exist"
"There must be a minimum of two files."
".csv" # needs to be added to the zoo name
"Error. File {} does not exist"

"Invalid zoo or does not exist."
"Invalid species or does not exist."
"Invalid name or does not exist."

"{}% of {} Zoo animals are sick. The sickest being {}."
" and "
"{} Zoos take better care of their animals!!!"
"{} Zoo takes better care of its animals!!!"
"{} Zoo spends ${} a month."
"{} zoos are the most expensive zoos!!!"
"{} Zoo is the most expensive zoo!!!"
"There are no twins in the zoo."
"Invalid choice. Choice must be a number or X."
"Thank you for your time at the Zoo!!!"
"\n{} and {} are twins separated at birth!!!\n"
"{}\n***************"
"Species ID: {}"
"Species: {}"
"Sex: {}\n"
"\nThey both:"
"\t\tAre {} years old."
"\t\tAre {}."
"\t\tTheir favorite game is {}."
"\t\tTheir favorite food is {}."
"\n{}\n***************"
"Species ID: {}"
"Species: {}"
"Age: {} years old"
"Sex: {}"
"Health: {}"
"Years at Zoo: {}"
"Favorite game: {}"
"Favorite food: {}"
"Personality: {}"
"Money spent per month: ${:,.2f}"

# Write all your function definitions before the main
def read_species_file():
    species_list = []
    species_dict = {}
    while True:
        file_name= input("\n:~Enter the Species ID file ~:")
        index = 1
        try:
            file = open(file_name, 'r')
            for line in file:
                species_name = line.strip()
                if species_name:
                    species_list.append(species_name)
                    species_dict[species_name] = {'ID':index, 'expense_frequency': None, 'expense_amount': None, 'sick':0}
                    index += 1
            file.close()
            break
        except FileNotFoundError:
            print("Error. File does not exist")

    return species_list, species_dict, file_name

def read_expenses_file(species_dict,workers_cost):
    workers_cost = 0
    other_expenses = {}
    while True:
        try:
            file_name= input("\n:~Enter the Expenses file ~:")
            file = open(file_name, 'r')
            for line in file:
                line = line.strip()
                expenses = line.split(',')
                if expenses[2] == "perday":
                    expenses[1] = float(expenses[1])
                    expenses[1] = expenses[1] * 30
                if expenses[2] == "peryear":
                    expenses[1] = float(expenses[1])
                    expenses[1] = expenses[1] / 12
                if expenses[0] in species_dict:
                    species_dict[expenses[0]]['expense_amount'] = float(expenses[1])
                    species_dict[expenses[0]]['expense_frequency'] = "permonth"
                if expenses[0] == 'workers':
                    workers_cost = float(expenses[1])
                else:
                    other_expenses[expenses[0]] = expenses[1]

            return species_dict,other_expenses,workers_cost

        except FileNotFoundError:
            print("Error. File does not exist")

def get_zoo_file_count():
    while True:
        zoo_file_count = int(input("\n:~Enter the number of Zoo files available (at least two) ~:"))
        if zoo_file_count < 2:
            print("There must be a minimum of two files.")
        else:
            return zoo_file_count


def get_zoo_file_names(zoo_file_count):
    zoo_name_list = []
    zoo_files_dict = {}
    for i in range(zoo_file_count):
        while True:
            zoo_name = input("\n:~Enter a Zoo name ~:")
            file_name = zoo_name + '.csv'

            try:
                file = open(file_name)
                zoo_name_list.append(zoo_name)
                file.close()
                zoo_files_dict[zoo_name] = file_name
                break
            except FileNotFoundError:
                print(f"Error. File {file_name} does not exist")

    return zoo_files_dict,zoo_name_list


def calculate_sick(species_dict, file, species_list):
    personality = ["shy", "courageous", "aggressive", "calm", "needy", "curious", "independent"]
    games = ["swim", "platforms", "handfeeding", "puzzles", "fake hunting", "swings", "hiding"]
    sick_counter = 0
    total_animals = 0
    species_id_map = {}
    sick_species_count = {}
    max_count = -1
    sickest_species = []

    index = 0
    species_count = len(species_list)

    while index < species_count:
        species_id_map[str(index + 1)] = species_list[index]
        index += 1

    for line in file:
        line = line.strip()
        animal_data = line.split(',')

        try:
            animal_data[2] = int(animal_data[2])
            animal_data[5] = int(animal_data[5])
        except ValueError:
            continue

        if line == "":
            continue
        elif animal_data[0].lower() == "species id":
            continue
        elif animal_data[8] not in personality:
            continue
        elif animal_data[6] not in games:
            continue
        elif animal_data[2]>30 or animal_data[2]<0:
            continue
        elif animal_data[5] >30 or animal_data[5] < 0:
            continue
        elif animal_data[5] > animal_data[2]:
            continue
        elif animal_data[1] == '' or animal_data[2] == ''or animal_data[3] == '' or animal_data[4] == '' or animal_data[5] == '' or animal_data[6] == ''or animal_data[7]==''or animal_data[8]=='':
            continue
        elif animal_data[4].lower() not in ['healthy','sick']:
            continue
        elif animal_data[3].lower() not in ['male','female']:
            continue
        else:
            species_id = animal_data[0]
            total_animals += 1
            health_status = animal_data[4]
            if health_status == "sick":
                sick_counter += 1
                if species_id in species_id_map:
                    species_name = species_id_map[species_id]
                    species_dict[species_name]['sick'] += 1

                    if species_name in sick_species_count:
                        sick_species_count[species_name] += 1
                    else:
                        sick_species_count[species_name] = 1
    average = int((sick_counter / (total_animals)) * 100)

    species_list_keys = list(sick_species_count.keys())
    key_count = len(species_list_keys)
    index = 0

    while index < key_count:
        species = species_list_keys[index]
        count = sick_species_count[species]

        if count > max_count:
            max_count = count
            sickest_species = []
            sickest_species.append(species)
        elif count == max_count:
            sickest_species.append(species)

        index += 1

    sickest_species.sort()
    formatted_species_list = ""

    for y,species in enumerate(sickest_species):
        if y == 0:
            formatted_species_list += species
        else:
            formatted_species_list += " and " + species

    return sick_counter, average, formatted_species_list, species_id_map



def calculate_cost_of_each_zoo(zoo_name_list, zoo_files_dict, expenses_data, species_list, other_expenses, workers_cost):
    personality = ["shy", "courageous", "aggressive", "calm", "needy", "curious", "independent"]
    games = ["swim", "platforms", "handfeeding", "puzzles", "fake hunting", "swings", "hiding"]
    zoo_expense_results = []
    zoo_name_count = len(zoo_name_list)
    species_count = len(species_list)
    species_id_map = {}

    for y in range(species_count):
        species_id_map[str(y + 1)] = species_list[y]

    for index in range(zoo_name_count):
        zoo_name = zoo_name_list[index]
        total_expense = 0
        file = open(zoo_files_dict[zoo_name], 'r')

        for line in file:

            fav_food_exp = 0
            if not line:
                break
            line = line.strip()
            animal_data = line.split(',')
            species_id = animal_data[0]
            try:
                animal_data[2] = int(animal_data[2])
                animal_data[5] = int(animal_data[5])
            except ValueError:
                continue
            if animal_data[7] in other_expenses:
                fav_food_exp = float(other_expenses[animal_data[7]])

            if animal_data[0] == "Species Id":
                continue
            elif animal_data[8] not in personality:
                continue
            elif animal_data[6] not in games:
                continue
            elif animal_data[2] > 30 or animal_data[2] < 0:
                continue
            elif animal_data[5] > 30 or animal_data[5] < 0:
                continue
            elif animal_data[5] > animal_data[2]:
                continue
            elif animal_data[1] == '' or animal_data[2] == '' or animal_data[3] == '' or animal_data[4] == '' or \
                    animal_data[5] == '' or animal_data[6] == '' or animal_data[7] == '' or animal_data[8] == '':
                continue
            elif animal_data[4] not in ['healthy', 'sick']:
                continue
            elif animal_data[3].lower() not in ['male','female']:
                continue
            else:
                if species_id in species_id_map:
                    species_name = species_id_map[species_id]
                    expense_amount = expenses_data[species_name]['expense_amount']
                    if expense_amount:
                        total_expense += float(expense_amount) + fav_food_exp

        file.close()
        total_expense += workers_cost
        total_expense = float(total_expense)
        zoo_expense_results.append((zoo_name, total_expense))

    zoo_expense_results.sort(key=itemgetter(0))

    for zoo_expense in zoo_expense_results:
        print(f"{zoo_expense[0].capitalize()} Zoo spends ${zoo_expense[1]:,.2f} a month.")

    max_expense = max(zoo_expense_results, key=itemgetter(1))[1]
    most_expensive_zoos = [zoo_expense[0].capitalize() for zoo_expense in zoo_expense_results if
                           zoo_expense[1] == max_expense]

    if len(most_expensive_zoos) > 1:
        result = most_expensive_zoos[0]
        for i in range(1, len(most_expensive_zoos)):
            result += " and " + most_expensive_zoos[i]
        print(f"{result} zoos are the most expensive zoos!!!")
    else:
        print(f"{most_expensive_zoos[0]} Zoo is the most expensive zoo!!!")


# def get_animal_info(zoo_files_dict, species_dict, other_expenses, species_list):
#     personality = ["shy", "courageous", "aggressive", "calm", "needy", "curious", "independent"]
#     games = ["swim", "platforms", "handfeeding", "puzzles", "fake hunting", "swings", "hiding"]
#
#     while True:
#         zoo_name = input(":~Enter a zoo ~:").lower()
#         if zoo_name not in zoo_files_dict:
#             print("Invalid zoo or does not exist.")
#             continue
#         while True:
#             species_name = input(":~Enter an animal species ~:").capitalize()
#             if species_name not in species_list:
#                 print("Invalid species or does not exist.")
#                 continue
#             else:
#                 break
#
#         while True:
#             animal_name = input(":~Enter the animal’s name ~:").capitalize()
#             file = open(zoo_files_dict[zoo_name], 'r')
#             animal_found = False
#
#             for line in file:
#                 line = line.strip().split(',')
#                 if line[1].capitalize() == animal_name and species_name == species_list[int(line[0]) - 1].capitalize():
#                     species_id = line[0]
#                     age = line[2]
#                     sex = line[3].lower()
#                     health = line[4].lower()
#                     years_at_zoo = line[5]
#                     favorite_game = line[6]
#                     favorite_food = line[7]
#                     personality_type = line[8]
#
#                     # Calculate monthly expenses
#                     food_expense = float(other_expenses.get(favorite_food, 0))
#                     animal_expense = float(species_dict[species_name]['expense_amount']) + food_expense
#
#                     # Print the details
#                     print()
#                     print(f"{animal_name}")
#                     print("***************")
#                     print(f"Species ID: {species_id}")
#                     print(f"Species: {species_name}")
#                     print(f"Age: {age} years old")
#                     print(f"Sex: {sex}")
#                     print(f"Health: {health}")
#                     print(f"Years at Zoo: {years_at_zoo}")
#                     print(f"Favorite game: {favorite_game}")
#                     print(f"Favorite food: {favorite_food}")
#                     print(f"Personality: {personality_type}")
#                     print(f"Money spent per month: ${animal_expense:,.2f}")
#                     animal_found = True
#                     break
#
#             file.close()
#
#             if animal_found:
#                 break
#             else:
#                 print("Invalid name or does not exist.")
#
#         if animal_found:
#             break
def get_animal_info(zoo_files_dict, species_dict, other_expenses, species_list):
    personality = ["shy", "courageous", "aggressive", "calm", "needy", "curious", "independent"]
    games = ["swim", "platforms", "handfeeding", "puzzles", "fake hunting", "swings", "hiding"]
    while True:
        # Prompt for a zoo
        while True:
            zoo_name = input(":~Enter a zoo ~:").lower()
            if zoo_name not in zoo_files_dict:
                print("Invalid zoo or does not exist.")
                continue
            break
        all_species = []
        zoo_file = open(zoo_files_dict[zoo_name], 'r')
        for line in zoo_file:
            line = line.strip()
            animal_data = line.split(',')
            species_id = animal_data[0]
            try:
                animal_data[2] = int(animal_data[2])
                animal_data[5] = int(animal_data[5])
            except ValueError:
                continue
            if animal_data[8] not in personality:
                continue
            elif animal_data[6] not in games:
                continue
            elif animal_data[2] > 30 or animal_data[2] < 0:
                continue
            elif animal_data[5] > 30 or animal_data[5] < 0:
                continue
            elif animal_data[5] > animal_data[2]:
                continue
            elif animal_data[1] == '' or animal_data[2] == '' or animal_data[3] == '' or animal_data[4] == '' or \
                    animal_data[5] == '' or animal_data[6] == '' or animal_data[7] == '' or animal_data[8] == '':
                continue
            elif animal_data[4] not in ['healthy', 'sick']:
                continue
            elif animal_data[3].lower() not in ['male', 'female']:
                continue
            else:
                all_species.append(species_id)
        zoo_file.close()

        # Prompt for a species
        while True:
            species_name = input(":~Enter an animal species ~:").capitalize()
            species_id_input = str(species_list.index(species_name) + 1) if species_name in species_list else None
            if species_id_input not in all_species:
                print("Invalid species or does not exist.")
                continue
            break

        # Prompt for an animal name
        while True:
            animal_name = input(":~Enter the animal’s name ~:").capitalize()
            file = open(zoo_files_dict[zoo_name], 'r')
            animal_found = False

            for line in file:
                line = line.strip().split(',')
                if line[1].capitalize() == animal_name and species_id_input == line[0]:
                    species_id = line[0]
                    age = line[2]
                    sex = line[3].lower()
                    health = line[4].lower()
                    years_at_zoo = line[5]
                    favorite_game = line[6]
                    favorite_food = line[7]
                    personality_type = line[8]
                    food_expense = float(other_expenses[favorite_food])
                    animal_expense = float(species_dict[species_name]['expense_amount']) + food_expense

                    # Print the details
                    print()
                    print(f"{animal_name}")
                    print("***************")
                    print(f"Species ID: {species_id}")
                    print(f"Species: {species_name}")
                    print(f"Age: {age} years old")
                    print(f"Sex: {sex}")
                    print(f"Health: {health}")
                    print(f"Years at Zoo: {years_at_zoo}")
                    print(f"Favorite game: {favorite_game}")
                    print(f"Favorite food: {favorite_food}")
                    print(f"Personality: {personality_type}")
                    print(f"Money spent per month: ${animal_expense:,.2f}")
                    animal_found = True
                    break

            file.close()

            if animal_found:
                return
            else:
                print("Invalid name or does not exist.")


def create_master_dictionary(file_gg,master_dict):
    for line in file_gg:
        parts = line.split(',')
        species_id = parts[0]
        if species_id.lower() == "species id":
            continue
        name = parts[1]
        age = parts[2]
        sex = parts[3]
        health = parts[4]
        years_at_zoo = parts[5]
        favorite_game = parts[6]
        favorite_food = parts[7] if len(parts) > 7 else None
        personality = parts[8] if len(parts) > 8 else None

        animal_dict = {
            "ID": species_id,
            "Age": age,
            "Sex": sex,
            "Health": health,
            "Years at Zoo": years_at_zoo,
            "Favorite Game": favorite_game,
            "Favorite Food": favorite_food,
            "Personality": personality
        }

        if species_id not in master_dict:
            master_dict[name] = []
        master_dict[name].append(animal_dict)



    return master_dict

def open_zoo_files(zoo_files_dict):
    zoo_file_handles = {}

    zoo_names = list(zoo_files_dict.keys())
    index = 0
    zoo_count = len(zoo_names)

    while index < zoo_count:
        zoo_name = zoo_names[index]
        file_name = zoo_files_dict[zoo_name]
        try:
            file_handle = open(file_name, 'r')
            zoo_file_handles[zoo_name] = file_handle
        except FileNotFoundError:
            print(f"Error. File {file_name} does not exist")
        index += 1

    return zoo_file_handles

def dict_new(zoo_file_handles, species_list, zoo_name_list):
    final = {}
    info = {}
    specie_count = len(species_list)
    personalities = ["shy", "courageous", "aggressive", "calm", "needy", "curious", "independent"]
    games = ["swim", "platforms", "handfeeding", "puzzles", "fake hunting", "swings", "hiding"]

    for y in range(specie_count):
        final[str(y + 1)] = species_list[y]

    x = 0
    while x < len(zoo_name_list):
        file = zoo_file_handles[zoo_name_list[x]]
        for line in file:
            line = line.strip().split(',')
            if len(line) < 9:
                continue
            try:
                line[2] = int(line[2])
                line[5] = int(line[5])
            except ValueError:
                continue

            if line[0].lower() == "species id":
                continue
            elif line[1] == '' or line[2] == '' or line[3] == '' or line[4] == '' or \
                line[5] == '' or line[6] == '' or line[7] == '' or line[8] == '':
                continue
            elif line[2] < 0 or line[2] > 30:
                continue
            elif line[5] < 0 or line[5] > 30:
                continue
            elif line[5] > line[2]:
                continue
            elif line[8] not in personalities:
                continue
            elif line[6] not in games:
                continue
            elif line[4] not in ['healthy', 'sick']:
                continue
            elif line[3].lower() not in ['male', 'female']:
                continue

            species_id = line[0]
            name = line[1]
            age = line[2]
            sex = line[3]
            favorite_food = line[7]
            favorite_game = line[6]
            personality = line[8]
            key = (age, personality, favorite_game, favorite_food)

            animal_details = {
                "ID": species_id,
                "Name": name,
                "Age": age,
                "Sex": sex,
                "Favorite Game": favorite_game,
                "Favorite Food": favorite_food,
                "Personality": personality
            }

            if key in info:
                info[key].append(animal_details)
            else:
                info[key] = [animal_details]

        x += 1

    pairs = []

    for details_list in info.values():
        if len(details_list) > 1:
            for i in range(len(details_list)):
                for j in range(i + 1, len(details_list)):
                    animal1 = details_list[i]
                    animal2 = details_list[j]
                    pair = [animal1, animal2]
                    sorted_pair = sorted(pair, key=lambda animal: animal['Name'])  # Sort the pair by name
                    pairs.append(sorted_pair)  # Append the sorted pair

    # Sort pairs by the name of the first animal only
    pairs.sort(key=lambda x: (x[0]["Name"], -ord(x[1]["Name"][0])))

    return pairs

def print_opt_four(sorted_pairs,species_list):
    pair_index = 0
    pairs_len = len(sorted_pairs)
    master_dict = {}

    while pair_index < pairs_len:
        pair = sorted_pairs[pair_index]
        print(f"\n{pair[0]['Name']} and {pair[1]['Name']} are twins separated at birth!!!\n")

        animal_details = []

        for animal in pair:
            species_id = animal['ID']
            name = animal['Name']
            age = animal['Age']
            sex = animal['Sex']
            favorite_game = animal['Favorite Game']
            favorite_food = animal['Favorite Food']
            personality = animal['Personality'].strip()
            specie = species_list[int(species_id) - 1]  # Map ID to species_list

            details = {
                "Species ID": species_id,
                "Species": specie,
                "Name": name,
                "Age": age,
                "Sex":sex,
                "Personality": personality,
                "Favorite Game": favorite_game,
                "Favorite Food": favorite_food
            }
            animal_details.append(details)

        # Print details for all found animals with the same name
        for details in animal_details:
            print(f"{details['Name'].capitalize()}\n***************")
            print(f"Species ID: {details['Species ID']}")
            print(f"Species: {details['Species']}")
            print(f"Sex: {details['Sex']}\n")



        if animal_details:  # Only print if we found animals
            print("\nThey both:")
            for details in animal_details:
                print(f"\t\tAre {details['Age']} years old.")
                print(f"\t\tAre {details['Personality']}.")
                print(f"\t\tTheir favorite game is {details['Favorite Game']}.")
                print(f"\t\tTheir favorite food is {details['Favorite Food']}.")
                break

        pair_index += 1


def main():
    banner = '''
        Zoos of the World!!
    ******************************************************************************************************************
    *                 ,-._                       **         (\-"""-/)           **      /\                 /\        *
    *              _.-'  '--.                    **          |     |            **     / \'._    (\_/)   _.'/ \       *
    *            .'      _  -`\_                 **          \ ^ ^ /  .-.       **    /_.''._'--('.')--'_.''._\      *
    *           / .----.`_.'----'                **           \_o_/  / /        **    | \_ / `;=/ " \=;` \ _/ |      *
    *           ;/     `                         **          /`   `\/  |        **     \/ `\__|`\___/`|__/`  \/      *
    *          /_;                               **         /       \  |        **      `      \(/|\)/       `       *
    *                                            **         \ (   ) /  |        **              " ` "                *
    *       ._      ._      ._      ._           **        / \_) (_/ \ /        **************************************
    *    _.-._)`\_.-._)`\_.-._)`\_.-._)`\_.-._   **       |   (\-/)   |         *
    *                                            **       \  --^o^--  /         *
    *    o                                       **        \ '.___.' /          *
    *   o      ______/~/~/~/__           /((     **       .'  \-=-/  '.         *
    *     o  // __            ====__    /_((     **      /   /`   `\   \        *
    *    o  //  @))       ))))      ===/__((     **     (//./       \.\\)        *
    *       ))           )))))))        __((     **      `"`         `"`        *
    *       \\     \)     ))))    __===\ _((      ********************************
    *        \\_______________====      \_((      *
    *                                    \((     *
    **********************************************
    '''
    print(banner)
    workers_cost = 0
    choices = ''' 
        Menu: 
            1: The healthiest zoo
            2: The most expensive zoo
            3: Individual information
            4: Twins separated at birth
            X: Quit the program
        '''

    species_list, species_dict,species_file = read_species_file()
    expenses_data,other_expenses,workers_cost = read_expenses_file(species_dict,workers_cost)
    zoo_file_count = get_zoo_file_count()
    zoo_files_dict, zoo_name_list = get_zoo_file_names(zoo_file_count)


    while True:
        print(choices)
        user_input = input("\n:~Input a choice ~:")
        if user_input == "1":
            zoo_results = []
            zoo_name_list.sort()
            for zoo_name in zoo_name_list:
                file = open(zoo_files_dict[zoo_name], 'r')
                sick_counter, average, sickest_species,species_id_map = calculate_sick(species_dict, file, species_list)
                if sickest_species:
                    print(f"{average}% of {zoo_name.capitalize()} Zoo animals are sick. The sickest being {sickest_species}.")
                else:
                    print(f"{average}% of {zoo_name.capitalize()} Zoo animals are sick. The sickest being none.")
                zoo_results.append((zoo_name, average))

            min_sick_percentage = min(zoo_results, key=itemgetter(1))[1]
            best_zoos = []
            for zoo_name, percentage in zoo_results:
                if percentage == min_sick_percentage:
                    best_zoos.append(zoo_name.capitalize())

            if len(best_zoos) > 1:
                result = best_zoos[0]
                for i in range(1, len(best_zoos)):
                    result += " and " + best_zoos[i]
                print(result + " Zoos take better care of their animals!!!")
            else:
                print(f"{best_zoos[0]} Zoo takes better care of its animals!!!")
        elif user_input == "2":
            calculate_cost_of_each_zoo(zoo_name_list, zoo_files_dict,expenses_data,species_list,other_expenses,workers_cost)
        elif user_input == "3":
            get_animal_info(zoo_files_dict, species_dict, other_expenses, species_list)
        elif user_input == "4":
            zoo_file_handles = open_zoo_files(zoo_files_dict)
            sorted_pairs = dict_new(zoo_file_handles, species_list, zoo_name_list)
            print_opt_four(sorted_pairs,species_list)
        elif user_input == "X" or user_input == 'x':
            print("Thank you for your time at the Zoo!!!")
        else:
            print("Invalid choice. Choice must be a number or X.")
# DO NOT MODIFY THE FOLLOWING 2 LINES.
# DO NOT WRITE ANYTHING AFTER THE FOLLOWING 2 LINES OF CODES
# All your code should be either in the main function
# or in a function.
if __name__ == "__main__":
    main()



