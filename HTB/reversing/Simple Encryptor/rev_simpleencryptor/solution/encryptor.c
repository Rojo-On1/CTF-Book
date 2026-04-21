#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int main(int argc, char* argv[]){
	int random_seed = atoi(argv[1]);
	
	unsigned char xor_key = 0;
	int swift_key = 0;
	srand(random_seed);

	printf("SEED: 0x%x\n",random_seed );
	puts("================");
	for (int i=0;i < atoi(argv[2]);i++){
		xor_key = rand();
		swift_key = rand() & 7;
		printf("xor_key: %d\n",xor_key );
		printf("swift_key: %d\n",swift_key );
		puts("============");
	}
}