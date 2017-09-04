import numpy as np 
import pylab as pl 
# Crea un vector (arreglo) con los valores del eje x 
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
# Crea un vector (arreglo) con los valores en el eje y para cada valor en el eje x
y= [0,0,0,0,1,1,1,0,0,0,0,0,0,1,2,1,1,2,2,2,2,2]
# Grafica el vector x contra el vector y 
pl.plot(x,y)
# Guarda la grafica en formato png
pl.savefig('temp1.png')
