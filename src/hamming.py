def reducent_bits(n):
    """
    Рассчитывает редуцентные биты p
    """
    p = 0
    while (2**p) < n + p + 1:
        p += 1
    return p

def encode(string):
    """
    Принимает строку из битов
    Кодирует строку кодом Хэмминга
    Возвращает строку битов в кодировке Хэмминга
    """
    bits = [int(b) for b in string]
    n = len(bits)
    p = reducent_bits(n)

    encoded_bits = [0] * (n + p)

    idx = 0
    for i in range(1, len(encoded_bits) + 1):
        if not(i & (i - 1) == 0):
            encoded_bits[i-1] = bits[idx]
            idx += 1

    for i in range(p):
        parity_pos = 2**i
        checked_bits = []
        for j in range(1, len(encoded_bits) + 1):
            if j & parity_pos:
                checked_bits.append(encoded_bits[j-1])

        encoded_bits[parity_pos-1] = sum(checked_bits) % 2

    return "".join(map(str, encoded_bits))

def decode(encoded_string):
    """
    Принимает закодированную строку из 0 и 1
    Декодирует и проверяет
    В случае ошибки возвращает -1 (успех) или индекс позиции с ошибкой
    """
    received_bits = [int(b) for b in encoded_string]
    n = len(received_bits)
    p = 0
    while (2**p) < n:
        p += 1

    status = 0

    for i in range(p):
        parity_pos = 2**i
        checked_bits = []
        for j in range(1, n + 1):
            if j & parity_pos:
                checked_bits.append(received_bits[j-1])

        if sum(checked_bits) % 2 != 0:
            status += parity_pos

    if status == 0:
        return -1
    else:
        return status