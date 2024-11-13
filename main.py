# Programmers:  Leif LaBianca
# Course:  CS151, Prof. Zee
# Due Date: Nov 14, 12:15
# Lab Assignment:  Lab 9
# Problem Statement:  read a list of names from txt files and assign them to tables of five in an output statement
# Data In: the txt files and their data
# Data Out:  an output statement of assigned seats
# Credits: all original code
# Input Files: yalew.txt, nweke.txt, isaacman.txt

# Purpose:  reads the names within files
# Parameters: yalew.txt, nweke.txt, isaacman.txt
# Return: all_names

def get_names(filename):
    # creates an empty list to fill in with names
    global all_names
    # opens and fills all_names with items from the desired text file
    file_data = open(filename)
    for name in file_data:
        all_names.append(name)
    file_data.close()
    return all_names

# Purpose:  assigns the seats for each guest
# Parameters: all_names
# Return: output statement of names
def assign_seats():
    # presets variables intrinsic to code
    global all_names
    table_count = 0
    seat_count = 1
    list_position = 0
    # loops through every name in all_names
    for name in all_names:
        # when the number of seats reaches 5, the table count goes up and the seat returns to 1
        if list_position % 5 == 0:
            table_count += 1
            seat_count = 1
        # prints aforementioned output statement
        print('~' * 25)
        print(f'Table {table_count}, Seat {seat_count}, {name}')
        print('~' * 25)
        # continually adds to seat count and list position
        list_position += 1
        seat_count += 1

all_names = []
passthru = False
while not passthru:
    file_name = input('Enter the name of the desired .txt file:\nPlease express the name without the .txt extension: ')
    if file_name == 'yalew':
        passthru = True
    elif file_name == 'isaacman':
        passthru = True
    elif file_name == 'nweke':
        passthru = True
    else:
        print('File could not be found. Try again\nEnter it EXACTLY as it is. Case sensetive\n')
get_names(f'{file_name}.txt')
assign_seats()


