typedef struct Rectangle {
int height ;
int width ; 
 } Rectangle_t ;

 void encoder(Rectangle_t* rectangle_struct, char **binary_view_of_struct);

void decoder(char ** binary_view_of_struct, Rectangle_t* rectangle_struct);


