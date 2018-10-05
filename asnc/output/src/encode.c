#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int encode_integer(int  number_to_be_encoded, char* temp){
    int k, i, l=0,number_to_be_encoded_log2 = log2(number_to_be_encoded);
	int bits_required_encode_number ,octets_req_to_encode_number, total_bits_required_to_encode;
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
	total_bits_required_to_encode = (octets_req_to_encode_number + 1 )*8 + 1;
	temp =(char *) realloc(temp, total_bits_required_to_encode* sizeof(char));
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
	printf("%s\n",temp);
    return total_bits_required_to_encode;
}