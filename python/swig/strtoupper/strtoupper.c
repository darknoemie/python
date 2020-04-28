/* strtoupper.c */

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
 
char Result[255];
 
char * strtoupper(const char * string) {
    int I;
    strcpy(Result,string);
    for(I = 0; I < strlen(Result); I++) {
        Result[I] = toupper(Result[I]);
    }
    return Result;
}
