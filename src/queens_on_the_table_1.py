import itertools

USER_SIDE = int(input("Write the lenght of the side of the field: "))


def is_valid_place(positions, n):
    for first_place in range(n):
        for second_place in range(first_place + 1, n):
            row1, column1 = positions[first_place]
            row2, column2 = positions[second_place]
            if abs(row1 - row2) == abs(column1 - column2):
                return False
    return True


def queen_placement(side):
    count = 0
    for rows in itertools.permutations(range(side)):
        queens = [(row, column) for row, column in enumerate(rows)]
        if is_valid_place(queens, side):
            count += 1
    return count

print("Count of right placing: ", queen_placement(USER_SIDE))