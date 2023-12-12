#ifndef FFT_UTILS_H
#define FFT_UTILS_H

/* C++ librairies */
#include <array>
#include <vector>
#include <complex>

/* C librairies */

/* External librairies */
#include "constants.h"

typedef std::complex<float> Complex;

void twiddle_factors(std::array<Complex, FFT_SIZE / 2> &t);
void bit_reverse_array(std::array<std::size_t, FFT_SIZE> &unscrambled);
void ite_dit_fft(std::vector<Complex> &x);

#endif