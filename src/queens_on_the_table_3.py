dictionary = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184]

def queens_placement(SIDE):

    def trees_from_rows(row, columns, main_diagonal, collateral_diagonal):

        if row == SIDE:
            return 1
        
        count = 0

        for column in range(SIDE):
            main = row - column
            collateral = row + column

            if (column not in columns and
                (main) not in main_diagonal and
                (collateral) not in collateral_diagonal):

                columns.add(column)
                main_diagonal.add(main)
                collateral_diagonal.add(collateral)

                count += trees_from_rows(row + 1, columns, main_diagonal, collateral_diagonal)

                columns.remove(column)
                main_diagonal.remove(main)
                collateral_diagonal.remove(collateral)
        
        return count

    return trees_from_rows(0, set(), set(), set())

USER_SIDE = int(input("Write the value of the side of the field: "))

if USER_SIDE <= len(dictionary):
    print("Count of right placing: ", dictionary[USER_SIDE])
else:
    USER_ANSWER = input("Your number is large, and the calculation may take a VERY long time. Are you willing to wait? Y/N")
    
    if USER_ANSWER in 'Yy':
        queens_placement(USER_SIDE)
    else:
        print("Enter a smaller side value please")