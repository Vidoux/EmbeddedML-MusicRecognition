#ifndef READAUFILE_H
#define READAUFILE_H

/* C++ librairies */
#include <fstream>

/* C librairies */

/* External librairies */

int read32Bits(std::ifstream &file);
int readSample(std::ifstream &file);

#endif