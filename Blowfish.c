#include <stdio.h>
#include <string.h>

int main() {
    char text[100], key;

    printf("Enter plaintext: ");
    scanf("%s", text);

    printf("Enter key character: ");
    scanf(" %c", &key);

    for(int i = 0; i < strlen(text); i++) {
        text[i] = text[i] ^ key;
    }

    printf("Ciphertext: %s", text);

    return 0;
}