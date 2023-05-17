#Tarea 5
#Computación Aplicada
#Alvarado Reyes, Ignacio               |A01656149
#Rangel García, Frida Berenice         |A01651385
#Villicaña Ibargüengoytia, José Rubén  |A01654347

import numpy as np
import math
from random import random
from random import gauss
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

#Definir la función de 3 variables
def f(x1,x2,x3):
  f = (x1) + (2*x2) + (x2*x3) - (x1**2) - (x2**2) - (x3**2)
  return f

#Parte de la graficación de la evolución de variables
def evol(u,v,w):
  plt.figure(1)
  plt.plot(u)
  plt.plot(v)
  plt.plot(w)
  plt.legend(('$x_1$', '$x_2$','$x_3$'))
  plt.ylim([-2,2])
  plt.title("Evolución de variables")
  plt.grid()
  plt.show()
  
def mutation(x,s):
  xn = x + s*gauss(0,1)
  while xn < -2 or xn > 2:
    xn = x + s*gauss(0,1)
  return xn

def sigma(s, g, m):
  ps = m/g
  c = 0.817
  if g%20 == 0:
    if ps > 0.2:
        s = s/c
    elif ps < 0.2:
        s = s*c
    else:
        s = s
  else:
      s = s
  return s
    
def main():
  #parámetros de simulación
  x1min, x1max, x2min, x2max, x3min, x3max = [-2, 2, -2, 2, -2, 2]
  gmax = 600                  #Se colocó 600 para obtener una mayor precisión.
  m = 0
  #individuo inicial
  x1 = 4*random()+x1min
  x2 = 4*random()+x2min
  x3 = 4*random()+x3min
  x10x20x30 = [round(x1,6),round(x2,6),round(x3,6)]
  print("x10,x20,x30:",x10x20x30)
  #primer padre
  padre = f(x1,x2,x3)
    
  s = 1
  #registro de individuos
  u = [x1]
  v = [x2]
  w = [x3]
  #ciclo principal
  for g in range(1, gmax):
    x1n = mutation(x1,s)
    x2n = mutation(x2,s)
    x3n = mutation(x3,s)
    hijo = f(x1n,x2n,x3n)
    if hijo > padre:            #Se modificó para obtener los máximos
      x1 = x1n
      x2 = x2n
      x3 = x3n
      m += 1
      padre = f(x1,x2,x3)
    else:
      x1 = x1
      x2 = x2
      x3 = x3
      m = m
    s = sigma(s, g, m)
    u.append(x1)
    v.append(x2)
    w.append(x3)
    
  x1fx2fx3f = [round(x1,6),round(x2,6),round(x3,6)]
  print("x1f,x2f,x3f:",x1fx2fx3f)

  evol(u,v,w)    
  
main()