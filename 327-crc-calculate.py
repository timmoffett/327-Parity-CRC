def crc_remainder(input_bitstring, polynomial_bitstring, initial_filler):
    '''
    Calculates the CRC remainder of a string of bits using a chosen polynomial.
    initial_filler should be '1' or '0'.
    '''
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = initial_filler * (len(polynomial_bitstring) - 1)
    input_padded_array = list(input_bitstring + initial_padding)
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
    return ''.join(input_padded_array)[len_input:]

def main():
    bitstring   = int(input("Bitstring: "), 2)
    divisor     = int(input("Divisor Bitstring: "), 2)
    filler   = int(input("Remainder Bitstring: "), 2)
    remainder = crc_remainder(bitstring, divisor, filler)
    print(bin(remainder))
    input()

if __name__ == '__main__':
    main()