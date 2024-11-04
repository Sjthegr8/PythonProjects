def get_file_input(prompt):
    while True:
        file_name = input(prompt)
        try:
            with open(file_name):
                return file_name
        except FileNotFoundError:
            print("Error. File does not exist.")

def max_grade(names_file):
    with open(names_file, 'r') as file:
        content = file.read()  # Read the entire file content
    names = content.splitlines()  # Split into lines

    while True:
        student_name = input(":~Enter a person name ~:")
        if student_name in names:
            print(f"{student_name} exists in the file.")
        else:
            print("Invalid name or does not exist.")


def main():
    names_file = get_file_input("Enter a student names file ~:")


if __name__ == "__main__":
    main()
