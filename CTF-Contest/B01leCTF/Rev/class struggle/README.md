Luego de refactorizar todo el texto y renombrar las variables quedaria algo asi y hacerle algunas modificaciones para poder bruteforcear la clave nos queda asi:

```c
#include <stdio.h>
#include <string.h>

unsigned char shift(unsigned char j,int counter){
  counter = counter & 7;
  return (j << counter) | (j>>(8-counter));
}

unsigned char second_round(unsigned char j,int counter){
  counter&=7;
  return(j >> counter) | ( j << (8-counter) );
}


first_round(unsigned char first_round,int index){
  first_round ^= (index *37);
  first_round=shift(first_round,(index+3)%7);
  first_round+=42;
  return first_round;
}
  
int check(const char *flag){
  const unsigned char cipher_flag []= {0x32,0xc0,0xbf,0x6c,0x61,0x85,0x5c,0xe4,0x40,0xd0,0x8f,0xa2,
                                      0xef,0x7c,0x4a,0x2,0x4,0x9f,0x37,0x18,0x68,0x97,0x39,0x33,0xbe,
                                      0xf1,0x20,0xf1,0x40,0x83,0x6,0x7e,0xf1,0x46,0xa6,0x47,0xfe,0xc3,
                                      0xc8,0x67,0x4,0x4d,0xba,0x10,0x9b,0x33
                                    };
  int flag_len=strlen(flag);
  //if(flag_len != sizeof(cipher_flag)){
  //  return  0;
  //}

     for(int index=0; index < flag_len; index++){
     unsigned char z=first_round(flag[index],index);
     unsigned char e=second_round((z&0xF0)|((~z)&0x0F), index%8);
     if(e != cipher_flag[index]){
       return 0;
       }
     }
 return 1;
 }
 
 int main(void){
   char flag[64];
   printf("Please input the flag: ");
   fgets(flag,sizeof(flag),stdin);
   char *endlined=strchr(flag,'\n');
   if(endlined){
     *endlined=0;
   }
   if(check(flag))
   {
     puts("Correct!");
   }
   else{
     puts("No.");
   }
   //return 0;
   return main();
 }
```

Compilamos el archivo.

```bash
gcc marx.c -o vuln
```

Nos creamos un bruteforce.py para obtener la contrasena de manera mas rapida:

```python
from pwn import *
import string
from time import sleep

p = process("./vuln")
flag_discovery = log.progress("FLAG")
flag = ""

while len(flag) < 46 :
    for char in string.printable[:-5]:
        p.sendline((flag + char).encode())
        if "correct" in p.recvS().lower():
            flag_discovery.status(flag)
            flag += char
            break
    #flag_discovery.failure("Something's wrong")
flag_discovery.success(flag)
```

Y tenemos la flag:
```
[+] Starting local process './vuln': pid 25663
[+] FLAG: bctf{seizing_the_m3m3s_0f_pr0ducti0n_32187ea8}
[*] Stopped process './vuln' (pid 25663)
```

