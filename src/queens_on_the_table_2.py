def queens_placement(side):
    columns = set()
    main_diagonal = set()
    collateral_diagonal = set()

    def trees_from_rows(row):
        if row == side:
            return 1

        count = 0

        for column in range(side):
            main = row - column
            collateral = row + column

            if (
                column not in columns
                and (main) not in main_diagonal
                and (collateral) not in collateral_diagonal
            ):
                columns.add(column)
                main_diagonal.add(main)
                collateral_diagonal.add(collateral)

                count += trees_from_rows(row + 1)

                columns.remove(column)
                main_diagonal.remove(main)
                collateral_diagonal.remove(collateral)

        return count

    return trees_from_rows(0)


user_side = int(input("Write the value of the side of the field: "))

print("Count of right placing: ", queens_placement(user_side))
