#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <string.h>


int decode_integer(char* input, int *decimal, int start_scanning_ptr){
	//*decimal =0 ;
        int octet_required_to_scan =0 , i;
        for(i=start_scanning_ptr;i<start_scanning_ptr+8;i++){
                if (*(input+i) == '1'){
                        octet_required_to_scan  = (octet_required_to_scan << 1 )+1;
                }
                else{
                        octet_required_to_scan = (octet_required_to_scan << 1 )+ 0;
                }
        }
        //printf("octet required to scan %d\n", octet_required_to_scan);
        for(i=start_scanning_ptr+8; i< start_scanning_ptr+  8*octet_required_to_scan + 8; i++){
                if(*(input+i)== '1'){
                        *decimal = (*decimal <<1) +1;
                }
                else{
                        *decimal = (*decimal<<1) + 0 ;
                }
        }
        //printf("decimal number %d\n",*decimal);
        //printf("======================================\n");
        //printf("returned %d\n\n", start_scanning_ptr + 8 + octet_required_to_scan*8);
         return start_scanning_ptr + 8 + octet_required_to_scan*8;
}
