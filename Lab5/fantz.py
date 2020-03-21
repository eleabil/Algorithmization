
def read_from_file(filename):
    line = open(filename).readline()
    numbers = line.split()
    return numbers


def create_array_of_binary_powers(n, input_string):
    power = 0
    binary_power = ''
    list_of_powers = []

    while len(binary_power) <= len(input_string):
        powered_number = pow(n, power)
        binary_power = bin(powered_number)[2:]
        list_of_powers.append(binary_power)
        for i in list_of_powers:
            if len(i) > len(input_string):
                list_of_powers.remove(i)
        power += 1

    return list_of_powers


if __name__ == '__main__':

    values = read_from_file('a.in')
    number = int(values[1])
    input_binary = values[0]
    print(input_binary)

    list_of_binary_powers = create_array_of_binary_powers(number, input_binary)
    print(list_of_binary_powers)

    i = len(list_of_binary_powers) - 1
    splits = 0

    while i >= 0:
        binary_power_from_list = list_of_binary_powers[i]
        print(binary_power_from_list)
        if binary_power_from_list in input_binary:
            splits = splits + input_binary.count(binary_power_from_list)
            input_binary = input_binary.replace(binary_power_from_list, '')
            print(splits)
            print(input_binary)
        i -= 1

    if input_binary == '':
        print("splits:")
        print(splits)

    else:
        print(-1)



