def crc_check(input_bitstring, polynomial_bitstring, check_value):
    '''
    Calculates the CRC check of a string of bits using a chosen polynomial. Courtesy of wikipedia
    '''
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = check_value
    input_padded_array = list(input_bitstring + initial_padding)
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
    return ('1' not in ''.join(input_padded_array)[len_input:])

def main():
    bitstring   = int(input("Bitstring: "), 2)
    divisor     = int(input("Divisor Bitstring: "), 2)
    remainder   = int(input("Remainder Bitstring: "), 2)
    crc_check(bitstring, divisor, remainder)

if __name__ == '__main__':
    main()
