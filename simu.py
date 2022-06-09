from matplotlib import pyplot as plt
from scipy import fftpack
from scipy.signal import hilbert
import numpy as np

plt.style.use('seaborn')

# Main Varaibles
sample_rate = 1000                                              # means we will have a data point every millisecond
start_time = 0
end_time = 1
time = np.arange(start_time, end_time, 1/sample_rate)
frequency = np.arange(-1 * (sample_rate / 2), (sample_rate / 2), 1/sample_rate)
A = 1

# Carrier Signal Variables
Ac = 5                                                          # 5volt
Fc = 100                                                        # 100khz
carrier_wave = Ac * np.cos(2 * np.pi * Fc * time)

# Modulating Signal Variables
Am = 1.5                                                        # 1.5volt
Fm = 2                                                          # 2khz
mt = Am * np.cos(2 * np.pi * Fm * time)

# FM 
kf = 10                                                         # 1000 rad / sec.volt
integerated_mt =  (Am / (2 * np.pi * Fm)) * np.sin(2 * np.pi * Fm * time)
FM = Ac * np.cos((2 * np.pi * Fc * time) + kf * integerated_mt)

# PM
kp = 10
PM = Ac * np.cos((2 * np.pi * Fc * time) + kp * mt)

# hilbert
mh = hilbert(mt).imag
USB = mt * carrier_wave - mh * Ac * np.sin(2 * np.pi * Fc * time)
LSB = mt * carrier_wave + mh * Ac * np.sin(2 * np.pi * Fc * time)

# [1][a] DSB-LC Time Domain

fig1, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True)          # Create subplots

ax1.plot(time, carrier_wave)                                    # Plot the carrier signal

ax1.set_xlabel("Time")                                          # labelling the x-axis
ax1.set_ylabel("Amplitude")                                     # labelling the y-axis
ax1.set_title("Carrier Wave")                                   # giving a title to the plot

ax2.plot(time, mt)                                              # plot the modulating signal

ax2.set_xlabel("Time")                                          # labelling the x-axis
ax2.set_ylabel("Amplitude")                                     # labelling the y-axis
ax2.set_title("Modulating Signal")                              # giving a title to the plot

ax3.plot(time, (Ac + mt) * carrier_wave)                        # plot the modulating signal

ax3.set_xlabel("Time")                                          # labelling the x-axis
ax3.set_ylabel("Amplitude")                                     # labelling the y-axis
ax3.set_title("AM DSB-LC signal")                               # giving a title to the plot

# [1][b] DSB-LC Frequency Domain

fig2, (bx1, bx2, bx3) = plt.subplots(nrows=3, ncols=1, sharex=True)          # Create subplots

freqs = fftpack.fftfreq(len(carrier_wave)) * sample_rate        # get the frequency range

fourier_coefficients_carrier_wave = fftpack.fft(carrier_wave)   # get the fourier coefficients for carrier wave

bx1.plot(freqs, np.abs(fourier_coefficients_carrier_wave))      # plot the absolute value of the coefficients to get the cosines

bx1.set_xlabel("Frequency")                                     # labelling the x-axis
bx1.set_ylabel("Amplitude")                                          # labelling the y-axis
bx1.set_title("Carrier Wave")                                   # giving a title to the plot

fourier_coefficients_modulating_signal = fftpack.fft(mt)        # get the fourier coefficients of the modulating signal

bx2.plot(freqs, np.abs(fourier_coefficients_modulating_signal)) # plot the absolute value of the coefficients to get the cosines

bx2.set_xlabel("Frequency")                                     # labelling the x-axis
bx2.set_ylabel("Amplitude")                                      # labelling the y-axis
bx2.set_title("Modulating Signal")                              # giving a title to the plot

fourier_coefficients_modulated_signal = fftpack.fft((Ac + mt) * carrier_wave)        # get the fourier coefficients of the modulated signal

bx3.plot(freqs, np.abs(fourier_coefficients_modulated_signal))  # plot the absolute value of the coefficients to get the cosines

bx3.set_xlabel("Frequency")                                     # labelling the x-axis
bx3.set_ylabel("(Ac + mt) * m(t)")                              # labelling the y-axis
bx3.set_title("Modulated Signal")                               # giving a title to the plot

# [2][a] DSB-SC Time Domain  

fig3, (cx1, cx2, cx3) = plt.subplots(nrows=3, ncols=1, sharex=True)          # Create subplots

cx1.plot(time, carrier_wave)                                    # Plot the carrier signal

cx1.set_xlabel("Time")                                          # labelling the x-axis
cx1.set_ylabel("Amplitude")                                     # labelling the y-axis
cx1.set_title("Carrier Wave")                                   # giving a title to the plot

cx2.plot(time, mt)                                              # plot the modulating signal

cx2.set_xlabel("Time")                                          # labelling the x-axis
cx2.set_ylabel("Amplitude")                                     # labelling the y-axis
cx2.set_title("Modulating Signal")                              # giving a title to the plot

cx3.plot(time, (mt) * carrier_wave)                             # plot the modulating signal

cx3.set_xlabel("Time")                                          # labelling the x-axis
cx3.set_ylabel("Amplitude")                                     # labelling the y-axis
cx3.set_title("AM SSB signal")                                  # giving a title to the plot

# [2][b] DSB-SC Frequency Domain 

fig4, (dx1, dx2, dx3) = plt.subplots(nrows=3, ncols=1, sharex=True)          # Create subplots

freqs = fftpack.fftfreq(len(carrier_wave)) * sample_rate        # get the frequency range

fourier_coefficients_carrier_wave = fftpack.fft(carrier_wave)   # get the fourier coefficients for carrier wave

dx1.plot(freqs, np.abs(fourier_coefficients_carrier_wave))      # plot the absolute value of the coefficients to get the cosines

dx1.set_xlabel("Frequency")                                     # labelling the x-axis
dx1.set_ylabel("Amplitude")                                          # labelling the y-axis
dx1.set_title("Carrier Wave")                                   # giving a title to the plot

fourier_coefficients_modulating_signal = fftpack.fft(mt)        # get the fourier coefficients of the modulating signal

dx2.plot(freqs, np.abs(fourier_coefficients_modulating_signal)) # plot the absolute value of the coefficients to get the cosines

dx2.set_xlabel("Frequency")                                     # labelling the x-axis
dx2.set_ylabel("Amplitude")                                      # labelling the y-axis
dx2.set_title("Modulating Signal")                              # giving a title to the plot

fourier_coefficients_modulated_signal = fftpack.fft((mt) * carrier_wave)        # get the fourier coefficients of the modulated signal

dx3.plot(freqs, np.abs(fourier_coefficients_modulated_signal))  # plot the absolute value of the coefficients to get the cosines

dx3.set_xlabel("Frequency")                                     # labelling the x-axis
dx3.set_ylabel("(mt) * m(t)")                                   # labelling the y-axis
dx3.set_title("Modulated Signal")                               # giving a title to the plot

# [3][a] SSB Time Domain 

fig5, (ex1, ex2, ex3, ex4, ex5) = plt.subplots(nrows=5, ncols=1, sharex=True)          # Create subplots

ex1.plot(time, carrier_wave)                                    # Plot the carrier signal

ex1.set_xlabel("Time")                                          # labelling the x-axis
ex1.set_ylabel("Amplitude")                                     # labelling the y-axis
ex1.set_title("Carrier Wave")                                   # giving a title to the plot

ex2.plot(time, mt)                                              # plot the modulating signal

ex2.set_xlabel("Time")                                          # labelling the x-axis
ex2.set_ylabel("Amplitude")                                     # labelling the y-axis
ex2.set_title("Modulating Signal")                              # giving a title to the plot

ex3.plot(time, mh)                                              # plot the hilbert modulating signal

ex3.set_xlabel("Time")                                          # labelling the x-axis
ex3.set_ylabel("Amplitude")                                     # labelling the y-axis
ex3.set_title("hilbert modulating signal Time Domain")          # giving a title to the plot

ex4.plot(time, USB)                                             # plot the hilbert modulating signal

ex4.set_xlabel("Time")                                          # labelling the x-axis
ex4.set_ylabel("Amplitude")                                     # labelling the y-axis
ex4.set_title("upper side band")                                # giving a title to the plot

ex5.plot(time, LSB)                                              # plot the hilbert modulating signal

ex5.set_xlabel("Time")                                          # labelling the x-axis
ex5.set_ylabel("Amplitude")                                     # labelling the y-axis
ex5.set_title("lower side band")                                # giving a title to the plot

# [3][b] SSB Frequency Domain 
fig6, (fx1, fx2, fx3, fx4, fx5) = plt.subplots(nrows=5, ncols=1, sharex=True)          # Create subplots

freqs = fftpack.fftfreq(len(carrier_wave)) * sample_rate        # get the frequency range

fourier_coefficients_carrier_wave = fftpack.fft(carrier_wave)   # get the fourier coefficients for carrier wave

fx1.plot(freqs, np.abs(fourier_coefficients_carrier_wave))      # plot the absolute value of the coefficients to get the cosines

fx1.set_xlabel("Frequency")                                     # labelling the x-axis
fx1.set_ylabel("Amplitude")                                          # labelling the y-axis
fx1.set_title("Carrier Wave")                                   # giving a title to the plot

fourier_coefficients_modulating_signal = fftpack.fft(mt)        # get the fourier coefficients of the modulating signal

fx2.plot(freqs, np.abs(fourier_coefficients_modulating_signal)) # plot the absolute value of the coefficients to get the cosines

fx2.set_xlabel("Frequency")                                     # labelling the x-axis
fx2.set_ylabel("Amplitude")                                      # labelling the y-axis
fx2.set_title("Modulating Signal")                              # giving a title to the plot

fourier_coefficients_modulated_signal = fftpack.fft(mh)         # get the fourier coefficients of the modulated signal

fx3.plot(freqs, np.abs(fourier_coefficients_modulated_signal))  # plot the absolute value of the coefficients to get the cosines

fx3.set_xlabel("Frequency")                                     # labelling the x-axis
fx3.set_ylabel("mh(f)")                                         # labelling the y-axis
fx3.set_title("Hilbert Modulating Signal")                      # giving a title to the plot

fourier_coefficients_modulated_signal = fftpack.fft(USB)        # get the fourier coefficients of the modulated signal

fx4.plot(freqs, np.abs(fourier_coefficients_modulated_signal))  # plot the absolute value of the coefficients to get the cosines

fx4.set_xlabel("Frequency")                                     # labelling the x-axis
fx4.set_ylabel("USB(f)")                                        # labelling the y-axis
fx4.set_title("Upper Side Band Signal")                         # giving a title to the plot

fourier_coefficients_modulated_signal = fftpack.fft(LSB)        # get the fourier coefficients of the modulated signal

fx5.plot(freqs, np.abs(fourier_coefficients_modulated_signal))  # plot the absolute value of the coefficients to get the cosines

fx5.set_xlabel("Frequency")                                     # labelling the x-axis
fx5.set_ylabel("LSB(f)")                                        # labelling the y-axis
fx5.set_title("Lower Side Band Signal")                         # giving a title to the plot



# [4][a] FM Time Domain 

fig7, (gx1, gx2, gx3) = plt.subplots(nrows=3, ncols=1, sharex=True)          # Create subplots

gx1.plot(time, carrier_wave)                                    # Plot the carrier signal

gx1.set_xlabel("Time")                                          # labelling the x-axis
gx1.set_ylabel("Amplitude")                                     # labelling the y-axis
gx1.set_title("Carrier Wave")                                   # giving a title to the plot

gx2.plot(time, mt)                                              # plot the modulating signal

gx2.set_xlabel("Time")                                          # labelling the x-axis
gx2.set_ylabel("Amplitude")                                     # labelling the y-axis
gx2.set_title("Modulating Signal")                              # giving a title to the plot

gx3.plot(time, FM)                                              # plot the modulating signal

gx3.set_xlabel("Time")                                          # labelling the x-axis
gx3.set_ylabel("Amplitude")                                     # labelling the y-axis
gx3.set_title("FM signal Time Domain")                          # giving a title to the plot

# [4][b] FM Frequency Domain

fig8, (hx1, hx2, hx3) = plt.subplots(nrows=3, ncols=1, sharex=True)          # Create subplots

freqs = fftpack.fftfreq(len(carrier_wave)) * sample_rate        # get the frequency range

fourier_coefficients_carrier_wave = fftpack.fft(carrier_wave)   # get the fourier coefficients for carrier wave

hx1.plot(freqs, np.abs(fourier_coefficients_carrier_wave))      # plot the absolute value of the coefficients to get the cosines

hx1.set_xlabel("Frequency")                                     # labelling the x-axis
hx1.set_ylabel("Amplitude")                                          # labelling the y-axis
hx1.set_title("Carrier Wave")                                   # giving a title to the plot

fourier_coefficients_modulating_signal = fftpack.fft(mt)        # get the fourier coefficients of the modulating signal

hx2.plot(freqs, np.abs(fourier_coefficients_modulating_signal)) # plot the absolute value of the coefficients to get the cosines

hx2.set_xlabel("Frequency")                                     # labelling the x-axis
hx2.set_ylabel("Amplitude")                                      # labelling the y-axis
hx2.set_title("Modulating Signal")                              # giving a title to the plot

fourier_coefficients_modulated_signal = fftpack.fft(FM)        # get the fourier coefficients of the modulated signal

hx3.plot(freqs, np.abs(fourier_coefficients_modulated_signal))  # plot the absolute value of the coefficients to get the cosines

hx3.set_xlabel("Frequency")                                     # labelling the x-axis
hx3.set_ylabel("Sfm(f)")                                        # labelling the y-axis
hx3.set_title("Modulated Signal")                               # giving a title to the plot

# [5][a] PM Time Domain

fig9, (ix1, ix2, ix3) = plt.subplots(nrows=3, ncols=1, sharex=True)          # Create subplots

ix1.plot(time, carrier_wave)                                    # Plot the carrier signal

ix1.set_xlabel("Time")                                          # labelling the x-axis
ix1.set_ylabel("Amplitude")                                     # labelling the y-axis
ix1.set_title("Carrier Wave")                                   # giving a title to the plot

ix2.plot(time, mt)                                              # plot the modulating signal

ix2.set_xlabel("Time")                                          # labelling the x-axis
ix2.set_ylabel("Amplitude")                                     # labelling the y-axis
ix2.set_title("Modulating Signal")                              # giving a title to the plot

ix3.plot(time, PM)                                              # plot the modulating signal

ix3.set_xlabel("Time")                                          # labelling the x-axis
ix3.set_ylabel("Amplitude")                                     # labelling the y-axis
ix3.set_title("PM signal Time Domain")                          # giving a title to the plot

# [5][b] PM Frequency Domain

fig10, (jx1, jx2, jx3) = plt.subplots(nrows=3, ncols=1, sharex=True)          # Create subplots

freqs = fftpack.fftfreq(len(carrier_wave)) * sample_rate        # get the frequency range

fourier_coefficients_carrier_wave = fftpack.fft(carrier_wave)   # get the fourier coefficients for carrier wave

jx1.plot(freqs, np.abs(fourier_coefficients_carrier_wave))      # plot the absolute value of the coefficients to get the cosines

jx1.set_xlabel("Frequency")                                     # labelling the x-axis
jx1.set_ylabel("Amplitude")                                          # labelling the y-axis
jx1.set_title("Carrier Wave")                                   # giving a title to the plot

fourier_coefficients_modulating_signal = fftpack.fft(mt)        # get the fourier coefficients of the modulating signal

jx2.plot(freqs, np.abs(fourier_coefficients_modulating_signal)) # plot the absolute value of the coefficients to get the cosines

jx2.set_xlabel("Frequency")                                     # labelling the x-axis
jx2.set_ylabel("Amplitude")                                      # labelling the y-axis
jx2.set_title("Modulating Signal")                              # giving a title to the plot

fourier_coefficients_modulated_signal = fftpack.fft(PM)         # get the fourier coefficients of the modulated signal

jx3.plot(freqs, np.abs(fourier_coefficients_modulated_signal))  # plot the absolute value of the coefficients to get the cosines

jx3.set_xlabel("Frequency")                                     # labelling the x-axis
jx3.set_ylabel("Amplitude")                                        # labelling the y-axis
jx3.set_title("Modulated Signal")                               # giving a title to the plot


plt.grid(True)                                                  # apply grid

plt.tight_layout()                                              # adjust the padding of the plot

plt.show()
