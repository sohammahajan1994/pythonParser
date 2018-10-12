#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "encode.h"
#include "decode.h"
#include "rectangle.h"

void encoder(Rectangle_t *rectangle_t_struct, char **output_binary_view){ 
	int bits_req_to_encode= 8;
	char temp_int[64];
	bits_req_to_encode += encode_integer(rectangle_t_struct->width, temp_int);
	*output_binary_view = realloc( *output_binary_view, bits_req_to_encode* sizeof(char));
	strcat(*output_binary_view, temp_int);
	bits_req_to_encode += encode_integer(rectangle_t_struct->height, temp_int);
	*output_binary_view = realloc( *output_binary_view, bits_req_to_encode* sizeof(char));
	strcat(*output_binary_view, temp_int);
}

void decoder(char *input_binary_view, Rectangle_t *rectangle_t_struct){
	int start_bit=0;
	start_bit = decode_integer(input_binary_view, &rectangle_t_struct->width, start_bit);
	start_bit = decode_integer(input_binary_view, &rectangle_t_struct->height, start_bit);
}
