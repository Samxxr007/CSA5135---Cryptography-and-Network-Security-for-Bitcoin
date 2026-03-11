#include <stdio.h>

int power(int base, int exp, int mod) {
    int result = 1;
    for(int i = 0; i < exp; i++)
        result = (result * base) % mod;
    return result;
}

int main() {
    int p = 3, q = 11;
    int n = p * q;
    int e = 3, d = 7;
    int msg, cipher, plain;

    printf("Enter message: ");
    scanf("%d", &msg);

    cipher = power(msg, e, n);
    printf("Encrypted message: %d\n", cipher);

    plain = power(cipher, d, n);
    printf("Decrypted message: %d", plain);

    return 0;
}