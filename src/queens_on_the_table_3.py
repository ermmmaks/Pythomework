dictionary = [
    0,
    1,
    0,
    0,
    2,
    10,
    4,
    40,
    92,
    352,
    724,
    2680,
    14200,
    73712,
    365596,
    2279184,
]
from queens_on_the_table_2 import queens_placement


def queens_placement(side):
    return trees_from_rows(0)


user_side = int(input("Write the value of the side of the field: "))

if user_side <= len(dictionary):
    print("Count of right placing: ", dictionary[user_side])
else:
    user_answer = input(
        "Your number is large, and the calculation may take a VERY long time. Are you willing to wait? Y/N"
    )

    if user_answer in "Yy":
        queens_placement(user_side)
    else:
        print("Enter a smaller side value please")
