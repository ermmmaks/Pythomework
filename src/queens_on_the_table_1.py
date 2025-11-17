import itertools

user_side = int(input("Write the lenght of the side of the field: "))


def is_valid_place(positions):
    for first_place in range(user_side):
        for second_place in range(first_place + 1, user_side):
            row1, column1 = positions[first_place]
            row2, column2 = positions[second_place]
            if abs(row1 - row2) == abs(column1 - column2):
                return False
    return True


def queen_placement(side):
    count = 0
    for rows in itertools.permutations(range(side)):
        queens = [(row, column) for row, column in enumerate(rows)]
        if is_valid_place(queens):
            count += 1
    return count


print("Count of right placing: ", queen_placement(user_side))
