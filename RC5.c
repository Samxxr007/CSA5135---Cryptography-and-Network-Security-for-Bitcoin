#include <stdio.h>
#include <stdint.h>

#define R 12

uint32_t S[2*(R+1)];

void rc5_key_schedule(uint32_t key){
    uint32_t P = 0xB7E15163, Q = 0x9E3779B9;
    S[0] = P;
    for(int i=1;i<2*(R+1);i++)
        S[i] = S[i-1] + Q;

    uint32_t A=0,B=0;
    for(int i=0;i<2*(R+1);i++){
        A = S[i] = (S[i] + A + B) << 3;
        B = key = (key + A + B) << (A+B);
    }
}

void rc5_encrypt(uint32_t *A, uint32_t *B){
    *A += S[0];
    *B += S[1];

    for(int i=1;i<=R;i++){
        *A = ((*A ^ *B) << *B) + S[2*i];
        *B = ((*B ^ *A) << *A) + S[2*i+1];
    }
}

int main(){
    uint32_t A,B,key;

    printf("Enter two numbers (plaintext block): ");
    scanf("%u %u",&A,&B);

    printf("Enter key: ");
    scanf("%u",&key);

    rc5_key_schedule(key);
    rc5_encrypt(&A,&B);

    printf("Ciphertext: %u %u",A,B);

    return 0;
}