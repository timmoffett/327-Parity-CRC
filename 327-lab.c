typedef unsigned uint;

uint parity( uint64_t x )
    {
    uint32_t v = x ^ (x >> 32);
    v ^= v >> 16;
    v ^= v >> 8;
    v ^= v >> 4;
    v ^= v >> 2;
    return (uint)(v ^ (v >> 1)) & 1;
    }

int main(int argc, char *argv[]) {

}