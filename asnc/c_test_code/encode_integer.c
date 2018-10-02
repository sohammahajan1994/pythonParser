#include <stdlib.h>
#include <math.h>
#include <stdio.h>


void encode_integer(int  int_t, char** temp){
      	int k, i, l=0, int_base_2 = log2(int_t);
	int output_length, output_length_bit;
	//printf("%d\n", int_base_2);
	if(pow(2, int_base_2) == int_t){
	   	output_length = int_base_2/8;
        }
	else{
		output_length = int_base_2/8 +1;
	}
	//printf("%d\n", output_length);
	output_length_bit = log2(output_length) +1;
	//printf("%d\n", output_length_bit);
	if(output_length_bit >8){
		return ;
	}
	*temp =(char *) malloc((output_length+1)*8* sizeof(char));
	for ( i = 7; i >= 0; i--) {
        	k = output_length >> i;
	        if (k & 1)
        		*(*temp +l) = '1';
        	else
	            	*(*temp +l) = '0';
		l++;
    	}
	//printf("%s\n",temp);
	//i = output_length *8;
	for ( i = (output_length*8) -1 ; i >= 0; i--) {
                k = int_t >> i;
                if (k & 1)
                        *(*temp +l) = '1';
                else
                        *(*temp +l) = '0';
                l++;
        }
	*(*temp+l) = '\0';
	//printf("%s\n",temp);


}

int main(){
	int int_t = 60;
	char* output = "outputi :- ";
	char* temp =NULL;
	encode_integer(int_t, &temp);
	printf("%s\n",temp);
	free(temp);
	return 0;
}
