#Modular Design

generate c code for encode_integer from pyhton code

read .h file 


1.  #Encoding
     a. get struct name as param with buff as output argument to encoder_function( S s, char* buff) <br  />
     b. parse struct members and call encode integer/ char /struct accordingly <br  /> 
     c. append returned string to buf i.e. outout argument <br />

2.  #Decoding
     a. get binary char * and struct as a output argument to decoder function <br />
     b. parse struct members and call decode integer / char/ struct respectively <br />
     c. add decoded value to the struct <br />
