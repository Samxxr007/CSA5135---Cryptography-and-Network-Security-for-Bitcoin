#include <stdio.h>
#include <math.h>

int gcd(int a,int b){
    while(b!=0){
        int t=b;
        b=a%b;
        a=t;
    }
    return a;
}

int modexp(int base,int exp,int mod){
    int result=1;
    while(exp>0){
        result=(result*base)%mod;
        exp--;
    }
    return result;
}

int main(){
    int p,q,n,phi,e=2,d=1,msg,cipher,plain;

    printf("Enter two prime numbers: ");
    scanf("%d %d",&p,&q);

    n=p*q;
    phi=(p-1)*(q-1);

    while(gcd(e,phi)!=1)
        e++;

    while((d*e)%phi!=1)
        d++;

    printf("Public Key (e,n) = (%d,%d)\n",e,n);
    printf("Private Key (d,n) = (%d,%d)\n",d,n);

    printf("Enter message: ");
    scanf("%d",&msg);

    cipher=modexp(msg,e,n);
    printf("Encrypted message: %d\n",cipher);

    plain=modexp(cipher,d,n);
    printf("Decrypted message: %d\n",plain);

    return 0;
}