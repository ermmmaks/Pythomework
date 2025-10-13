USER_STR1 = str(input("Введите первую строку: "))
USER_STR2 = str(input("Введите вторую строку: "))
ALPHABET = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"[::-1]
MIN_LEN = min(len(USER_STR1), len(USER_STR2))

# 1) чем символ дальше от начала алфавита (z), тем он старше
# 2) чем меньше длина строки, тем она старше


def lexic_order(string1, string2):
    for latin in string1 + string2:
        if latin not in ALPHABET:
            return "Используйте только латиницу!"

    for let in range(0, MIN_LEN):
        let_s1 = string1[let]
        let_s2 = string2[let]

        if (let_s1 != let_s2) or (
            let == MIN_LEN - 1 and let_s1 == let_s2
        ):  # сравнение возможно, если:
            # 1. всретились разные буквы
            # 2. буквы одинаковые вплоть до последнего символа одной из строк
            if (ALPHABET.index(let_s1) > ALPHABET.index(let_s2)) or (
                len(string1) < len(string2)
                and (let_s1 == let_s2)
                and let == MIN_LEN - 1
            ):
                return "Первая строка старше, чем Вторая"
            elif (ALPHABET.index(let_s2) > ALPHABET.index(let_s1)) or (
                len(string1) > len(string2)
                and (let_s1 == let_s2)
                and let == MIN_LEN - 1
            ):
                return "Вторая строка старше, чем Первая"
    return "Строки идентичны"


print(lexic_order(USER_STR1, USER_STR2))
