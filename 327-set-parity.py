def calculate_parity( n ): 
    parity = 0
    while n: 
        parity = ~parity 
        n = n & (n - 1) 
    return abs(parity)

def get_parity( n ):
    parity_bit = n & bin(1)
    return parity_bit


def main():
    binary          = int(input("Binary input: "),2)
    parity_bit      = calculate_parity(binary)
    binary_str      = binary << 1
    binary_output   = binary_str | parity_bit
    print("Parity Bit: ", parity_bit)
    print(bin(binary_str))
    print(bin(binary_output))

if __name__ == '__main__':
    main()