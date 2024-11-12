def get_names(yalew.txt, nweke.txt, isaacman.txt):
    all_names = []
    yalew_data = open(yalew.txt, 'r')
    for name in yalew_data:
        all_names.append(name)
    yalew_data.close()
    nweke_data = open(nweke.txt, 'r')
    for name in nweke_data:
        all_names.append(name)
    nweke_data.close()
    isaacman_data = open(isaacman.txt, 'r')
    for name in isaacman_data:
        all_names.append(name)
    isaacman_data.close()
    return all_names

def assign_seats(all_names):
    table_count = 0
    seat_count = 1
    list_position = 0
    for name in all_names:
        if list_position % 5 == 0:
            table_count += 1
            seat_count = 1
        print('~' * 25)
        print(f'Table {table_count}, Seat {seat_count}, {name}')
        print('~' * 25)
        list_position += 1
        seat_count += 1

def main()
    get_names(yalew.txt, nweke.txt, isaacman.txt)
    assign_seats(all_names)


