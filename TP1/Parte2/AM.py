#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:30:29 2020

@author: fran
"""


# =============================================================================
# Escriba un scrip de python que genere
# un archivo de una senoidal de 1kHz
# modulada en AM al 50% con una 
# frecuencia de portadora de 1MHz.
# =============================================================================

import numpy as np
import matplotlib.pyplot as plot

fmsg = 1e3 #frecuencia del mensaje
fc = 1e6 #frecuencia de la portadora
N = 10000 #cantidad de muestras
m=0.5
t = np.linspace(0,1e-3,N)
ts = t[1]
fs = 1/ts
print(f"Frecuencia de muestreo:\t{fs}")
def mod_am(mensaje, carrier, indice):
    return ((1+indice*mensaje)*carrier)

# Mensaje
msg = np.sin(2*np.pi*fmsg*t,dtype="float32")
print(f"Mensaje:\t {msg}")
plot.figure()
plot.title("Mensaje")
plot.plot(t,msg)
plot.grid(1)

# Portadora
portadora = np.exp(2j*np.pi*fc*t,dtype="complex64")
print(f"Portadora:\t {portadora}")
plot.figure()
plot.title("Portadora")
plot.plot(t,portadora)
plot.grid(1)

AM= mod_am(msg,portadora,m)
print(f"Modulada:\t {AM}")
plot.figure()
plot.title("Modulada")
plot.plot(t,AM)
plot.grid(1)


file = open("AM.dat","wb")
np.ndarray.tofile(AM,file,sep="",format="%f")
file.close()

a=np.fromfile(open("AM.dat"),dtype=np.complex64)
plot.figure()
plot.plot(a)