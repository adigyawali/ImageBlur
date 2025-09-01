#include <stdio.h>
#include <stdlib.h>


//Struct to hold the rgb values
typedef struct{
    unsigned char r, b, g
} Pixel;

// Main Function
int main(int argc, char *argv[]){

    printf("Hello does this work");
}

typedef struct {
    int width;
    int height;
    Pixel *data; // 1D array of pixels
} Image;

