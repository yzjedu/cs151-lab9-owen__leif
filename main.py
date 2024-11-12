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
def get_names(yalew.txt, nweke.txt, isaacman.txt):
    # creates an empty list to fill in with names
    all_names = []
    # opens and fills all_names with items from yalew.txt
    yalew_data = open(yalew.txt, 'r')
    for name in yalew_data:
        all_names.append(name)
    yalew_data.close()
    # opens and fills all_names with items from nweke.txt
    nweke_data = open(nweke.txt, 'r')
    for name in nweke_data:
        all_names.append(name)
    nweke_data.close()
    # opens and fills all_names with items from isaacman.txt
    isaacman_data = open(isaacman.txt, 'r')
    for name in isaacman_data:
        all_names.append(name)
    isaacman_data.close()
    return all_names

# Purpose:  assigns the seats for each guest
# Parameters: all_names
# Return: output statement of names
def assign_seats(all_names):
    # presets variables intrinsic to code
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

# Purpose:  runs main function
# Parameters:
# Return:
def main():
    get_names(yalew.txt, nweke.txt, isaacman.txt)
    assign_seats(all_names)


