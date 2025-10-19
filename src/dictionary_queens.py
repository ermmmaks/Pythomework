variations = []


def queens_placement(side):
    def trees_from_rows(row, columns, main_diagonal, collateral_diagonal):
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

                count += trees_from_rows(
                    row + 1, columns, main_diagonal, collateral_diagonal
                )

                columns.remove(column)
                main_diagonal.remove(main)
                collateral_diagonal.remove(collateral)

        return count

    return trees_from_rows(0, set(), set(), set())


for i in range(15):
    variations.append(queens_placement(i))
    print(variations)
