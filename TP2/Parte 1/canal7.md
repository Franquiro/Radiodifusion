## Captura Canal 7
a) implementar un demodulador de video que permita extraer la señal de video transmitida.
    
>__canal7.grc__ muestra, por un lado la señal recibida, y por otro la señal de video demodulada.

b) Medir de la señal de video demodulada previamente la frecuencia de barrido horizontal.

>En el archivo __Mediciones.odt__ se puede observar que el tiempo de barrido horizontal es de 64 micro segundos, dando una frecuencia de 15,625KHz. 

c) Encontrar y describir el pulso de borrado vertical y explicar las diferencias entre el pulso de borrado del campo par y campo impar.
> El pulso de borrado vertical consta de: 
>* 5 pulsos de pre ecualización que toman 2.5 lineas.
>* 5 Pulsos de sincronismo vertical que toman otras 2.5 lineas.
>* 5 pulsos de post ecualización que toman otras 2.5 lineas
>* 12.5 pulsos de blanqueo que toman 12.5 lineas de los cuales algunos pueden ser utilizados para enviar señales de prueba o teletexto.
>
>Para el __campo impar__, La señal arranca al principio de la primer linea y termina en la mitad de la última. 
>
>Para el __campo par__, la señal arrancará en la mitad de la primer linea y terminará al final de la última.