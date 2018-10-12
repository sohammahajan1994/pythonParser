#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "rectangle.h"


main(){
  Rectangle_t *rect , *rect_1;
  char* b_v_s= malloc(sizeof(char)*4);
  rect = malloc(sizeof(Rectangle_t));
  rect_1 = calloc(1, sizeof(Rectangle_t));
  
  rect->width = 12;
  rect->height = 17;
  encoder(rect, &b_v_s);
  printf("\n%s\n", b_v_s);


  printf("%d\n", rect_1->height);
  printf("%d\n", rect_1->width);

  decoder(b_v_s, rect_1);

  printf("%d\n", rect_1->height);
  printf("%d\n", rect_1->width);

}

//gcc -Iinclude/ main.c rectangle.c encode.c decode.c -lm
