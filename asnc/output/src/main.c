#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "rectangle.h"


main(){
  Rectangle_t* rect;
  char* b_v_s= malloc(sizeof(char)*4);
  *(b_v_s +0) = 'S';
  *(b_v_s + 1) = '\0';

  printf(" jai hind \n");
  rect = malloc(sizeof(*rect));
  rect->width = 12;
  rect->height = 17;
  encoder(rect, &b_v_s);
  printf("\n%s\n", b_v_s);

}

//gcc -Iinclude/ main.c rectangle.c encode.c -lm
