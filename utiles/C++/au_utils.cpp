#include "au_utils.h"

int read32Bits(std::ifstream &file){
    int number=0;
    for (int i=0; i<4; i++){
        number = number << 8 | (int)file.get();
    }
    return number;
}

int readSample(std::ifstream &file){
    short sample=0;
    unsigned char part;
    for (int i=0; i<2; i++){
        part=(unsigned char)file.get();
        sample=sample << 8 | (short)part;
    }
    return (int)sample;
}