# Algorithm Document
#### PLEASE! PLEASE! PLEASE! stop

* Purpose:  reads the names within files
* Name: get_names
* Parameters: yalew.txt, nweke.txt, isaacman.txt
* Return: all_names
* Algorithm:
1. Define an empty list with a name like "all_names"
2. Open the text files containing the guests
3. read each name in the file
4. for each name in the respective file:
    1. append the name to "all_names"
5. close the text files
6. return "all_names"

* Purpose:  assigns the seats for each guest
* Name: assign_seats
* Parameters: all_names
* Return: output statement of names
* Algorithm:
1. assign a variable with a name like "table_count" to a value of zero
2. assign another variable with a name like "seat_count" to a value of one
3. assign a third variable with a name like "list_position" to a value of zero
3. for each name in list all_names:
    1. if "list_position" when divided by five has a remainder of exactly zero:
         1. add 1 to the current value of "table_count"
       2. set "seat_count" equal to 1
    2. print 25 tildes
   3. print the table count, seat count, and name of the person occupying the seat
   4. print 25 tildes
   5. add 1 to the current value of "list_position"
   6. add 1 to the current value of "seat_count"
   
* Purpose:  runs the main function
* Name: main
* Parameters: none
* Return: nothing
* Algorithm:
1. run "get_names"
2. run "assign_seats"

