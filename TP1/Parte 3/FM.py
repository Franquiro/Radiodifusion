# Escriba un script de python que permita modular 
# una señal “mensaje” en FM y reciba como parametro 
# ademas la desfiacion maxima de frecuencia y genere 
# una señal de FM en banda base

import numpy as np 
import matplotlib.pyplot as plot
from scipy import signal as dsp

N = 10000
t = np.linspace(0,1e-3,N)
fc = 1e6 # Freq de carrier
deltaf = 10e3 # desviacion de frecuencias
fmsg = 100e3 # Freq de mensaje
Vc = 10 # Tension de carrier
Vm = 1


def mod_fm(Ac,Amsg,deltaf,fc,fmsg):
    return Ac*np.cos(2*np.pi*fc*t+(Amsg*deltaf/fmsg)*np.sin(2*np.pi*fmsg*t),dtype="complex64")

fm = mod_fm(Vc,Vm,deltaf,fc,fmsg)

plot.figure()
plot.plot(t,fm)

espectro = np.abs(np.fft.fft(fm))

fs = 1/t[1]
print(f"Frecuencia de sampling: {fs}")
freq = np.linspace(-fs/2,fs/2,N)
plot.figure()
plot.plot(freq,espectro)


file = open("FM.dat","wb")
np.ndarray.tofile(fm,file,sep="",format="%f")
file.close()