#include <stdio.h>
#include <string.h>

int main() {
    char text[100];
    int hash = 0;

    printf("Enter message: ");
    scanf("%s", text);

    for(int i = 0; i < strlen(text); i++)
        hash = hash + text[i];

    printf("MD5 Hash value: %d", hash);

    return 0;
}