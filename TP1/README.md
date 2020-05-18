# TP1
## Generador y QTsinks (Tp1a.grc)
a)  Conectar un bloque signal source a un time-sink y frequency sink
    i) Utilizar ambos tipos de salida ( float – complejo)

b. Corregir el efecto de la ventana del frequency sink de manera que una apmlitud de 1 genere un espectro de amplitud 0dB (__Tp1a1.grc__)

c. Agregar slider de amplitud y frecuencia (__Tp1b.grc__)

d. En qué caso el espectro es simétrico y por qué?
    
    El espectro es simétrico cuando la señal es real.

e. El archivo  espectro_2M.dat hay una captura del espectro centrado en 95.1MHz con una frecuencia de muestreo de 2MSps.¿Cómo está relacionado el  sample rate con el espectro obtenido? (__Tp1d.grc__)

    El espectro obtenido tendrá mejor resolución si se muestrea mas rápido.

f. utilizando el archivo  espectro_2M.dat, Implemente filtros que permitan seleccionar cada una de las emisoras. Utilice un Frequency Sink con varias entradas para comparar el espectro antes y después del filtro. (__TP1f.grc__)

g. Determinar cual es el nivel de potencia recibido de cada una de las estaciones capturadas en espectro_2M.dat (__Tp1e.grc__)

h. Conectar un bloque signal source a un file sink. 
    Escriba un scrip de python que levante el anchivo generado por el file sink y calcule su espectro implementando distintas ventanas, la potencia de la señal. (__Tp1g.grc__)	
## Generación y recepción de AM/DBL
### Recepción de AM
Escriba un scrip de python que genere un archivo de una senoidal de 1kHz modulada en AM al 50% con una frecuencia de portadora de 1MHz.
AM.py

a) Implementar un detector sincronico en GNURadio que recupere el mensaje(__AM.grc__)

b) Idem a pero utilizando detector de envolvente(__AM.grc__)

### Transmisión de AM
a) Diseñe un transmisor de AM en GNUradio de índice de modulación variable y utilice TpAMa.grc en otra PC para su verificación. V (__TPAMb.grc__)

### Recepción de FM en GNURadio
Recepción de FM

a) Utilizando el archivo espectro_2M.dat y  el bloque quadrature demod y obtenga la salida de audio demodulada de cada estación y a través de un selector poder conectar cada señal de audio a la placa de sonido.
(__Tp2a.grc__)

b) Escriba un script de python que permita modular una señal “mensaje” en FM y reciba como parametro ademas la desfiacion maxima de frecuencia y genere una señal de FM en banda base. (__FM.py__)

Entendiendo la función del bloque quadrature demod implemente en GNURadio la medición de desviación de portadora pico y RMS, utilice para este ejercicio la señal generada por FM.py.(__Tp2b.grc__)

c) Utilizando la captura radio.dat, demodule la estación comercial de FM e identifique las señales MONO, PILOTO y ESTEREO.
    i. Impleente los 3 filtros que permitan separar cada una de ellas.
    (__Tp2c.grc__)

d. Utilizando la captura radio.dat, demodule una estación comercial de FM e implemente un diagrama que permita separar el canal R y L
(__Tp2d.grc__)


### Generación de FM en GNURadio
Generación de FM

a) Utilizando un bloque cuad mod y QT frequency sink, modular un signal source senoidal de 10kHz con una desviación de 10kHz. Verificar el espectro obtenido con las amplitudes obtenidas aplicando los coeficientes de Besell.
(__Tp3a.grc__)

b) Implemente un codificador estéreo según las recomendaciones de la norma argentina. Debe obtener una señal MPX.
(__Tp3d.grc__)

c) Utilizando el codificador estereo genere un archivo que luego sea decodificado por el Tp2d.grc y verifique poder recuperar correctamente L y R



