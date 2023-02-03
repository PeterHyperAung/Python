def binary_to_denary(num):
    denary = 0
    num_list = list(str(num))
    num_list.reverse()
    for idx in range(0, len(num_list)):
        denary += int(num_list[idx]) * (2 ** idx)
    return denary


print(binary_to_denary('11111111'))


def denary_to_binary(num):
    binary = ''
    current = num
    while True:
        remainder = current % 2
        current //= 2
        if remainder == 0 and current == 0:
            break
        binary = str(remainder) + binary

    return int(binary)


print(denary_to_binary(255))
