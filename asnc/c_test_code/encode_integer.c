#include <stdlib.h>
#include <math.h>
#include <stdio.h>


void encode_integer(int  number_to_be_encoded, char* temp){
    	int k, i, l=0,number_to_be_encoded_log2 = log2(number_to_be_encoded);
	int bits_required_encode_number ,octets_req_to_encode_number;
	//printf("%d\n", number_to_be_encoded_log2);
	if(pow(2, number_to_be_encoded_log2) == number_to_be_encoded){
		bits_required_encode_number = number_to_be_encoded_log2;
	}
	else{
		bits_required_encode_number = number_to_be_encoded_log2+1;
	}
	if(bits_required_encode_number%8 ==0){
		 octets_req_to_encode_number = bits_required_encode_number/8 ;
	}
	else{
		 octets_req_to_encode_number = bits_required_encode_number/8 +1;
	}
	//printf("%d\n", bits_required_encode_number);
	//printf("%d\n", octets_req_to_encode_number);
	temp =(char *) realloc(temp,(octets_req_to_encode_number+1)*8* sizeof(char));
	for ( i = 7; i >= 0; i--) {
        	k = octets_req_to_encode_number >> i;
	        if (k & 1)
        		*(temp +l) = '1';
        	else
	            	*(temp +l) = '0';
		l++;
    	}
	//printf("%s\n",temp);
	for ( i = (octets_req_to_encode_number*8) -1 ; i >= 0; i--) {
                k = number_to_be_encoded >> i;
                if (k & 1)
                        *(temp +l) = '1';
                else
                        *(temp +l) = '0';
                l++;
        }
	*(temp+l) = '\0';
	//printf("%s\n",temp);


}

int main(){
	int number_to_be_encoded = 266;
	char* temp = malloc (sizeof(char));
	encode_integer(number_to_be_encoded, temp);
	printf("%s\n",temp);
	free(temp);
	return 0;
}
