#Considere um balde cuja base possui raio  **r1**  e altura igual ao diâmetro da base. Considere também uma esfera de raio  **r2**  cheia de água. 
#Faça um programa que verifique se o volume da esfera cabe no balde, dados os valores de  **r1**  e  **r2**.

#Para resolver este problema, encontrei três possibilidades para resolvê-lo:

#**Forma 1**
from math import pi
def VerificaVolume(raio_balde, raio_esfera):
  if raio_balde <= 0:
    print('Medida Inadequada')
  elif raio_esfera <=0:
    print('Medida Inadequada')
  else:  
    vol_balde = 2*pi*raio_balde**3
    vol_esfera = 4/3*pi*raio_esfera**3

    if vol_esfera > vol_balde:
      print('O volume da esfera não cabe no balde')
    else:
      print('O volume da esfera cabe no balde')


#**Forma 2**
from math import pi
def VerificaVolumee(raio_balde, raio_esfera):
  if raio_balde <= 0 or raio_esfera <= 0:
    print('Medida Inadequada')
  else:  
    vol_balde = 2*pi*raio_balde**3
    vol_esfera = 4/3*pi*raio_esfera**3

    if vol_esfera > vol_balde:
      print('O volume da esfera não cabe no balde')


#**Forma 3**
from math import pi
def VerificaVolumee(raio_balde, raio_esfera):
  if raio_balde > 0 and raio_esfera > 0:
    vol_balde = 2*pi*raio_balde**3
    vol_esfera = 4/3*pi*raio_esfera**3

    if vol_esfera > vol_balde:
      print('O volume da esfera não cabe no balde')
    else:
      print('O volume da esfera cabe no balde')
  else:
     print('Medida Inadequada')
    else:
      print('O volume da esfera cabe no balde')
