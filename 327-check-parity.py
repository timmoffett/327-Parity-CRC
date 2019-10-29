def calculate_parity( n ): 
    parity = 0
    while n: 
        parity = ~parity 
        n = n & (n - 1) 
    return abs(parity)


def get_parity( n ):
    parity_bit = n & 1
    return parity_bit


def main():
    binary_parity       = int(input("Binary input: "),2)
    parity_bit          = get_parity(binary_parity)
    binary              = binary_parity >> 1
    calculated_parity   = calculate_parity(binary)
    print("Parity Bit: ", parity_bit)
    print("Calculated Parity Bit: ", calculated_parity)
    if (parity_bit == calculated_parity):
        print("Parity Match")
    else:
        print("Parity Mismatch")

if __name__ == '__main__':
    main()