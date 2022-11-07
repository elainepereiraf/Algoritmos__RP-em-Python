#Considere um balde cuja base possui raio **r1** e altura igual ao diâmetro da base. Considere também uma esfera de raio **r2** cheia de água.
#Faça um programa que verifica se o volume da esfera cabe no balde, dados **r1** e **r1**.

#Para resolver este problema, encontrei três possibilidades para resolvê-lo:


#**Forma 1**
da  importação de matemática  pi 
def  VerificaVolume ( raio_balde , raio_esfera ):
  se  raio_balde  <=  0 :
    print ( 'Medida Inadequada' )
  elif  raio_esfera  <= 0 :
    print ( 'Medida Inadequada' )
  mais :  
    vol_balde  =  2 * pi * raio_balde ** 3
    vol_esfera  =  4/3 * pi * raio_esfera ** 3

    if  vol_esfera  >  vol_balde :
      print ( 'O volume da esfera não cabe no balde' )
    mais :
      print ( 'O volume da esfera cabe no balde' )


#**Forma 2**
da  importação de matemática  pi 
def  VerificaVolumee ( raio_balde , raio_esfera ):
  se  raio_balde  <=  0  ou  raio_esfera  <=  0 :
    print ( 'Medida Inadequada' )
  mais :  
    vol_balde  =  2 * pi * raio_balde ** 3
    vol_esfera  =  4/3 * pi * raio_esfera ** 3

    if  vol_esfera  >  vol_balde :
      print ( 'O volume da esfera não cabe no balde' )

      
#**Forma 3**
da  importação de matemática  pi 
def  VerificaVolumee ( raio_balde , raio_esfera ):
  se  raio_balde  >  0  e  raio_esfera  >  0 :
    vol_balde  =  2 * pi * raio_balde ** 3
    vol_esfera  =  4/3 * pi * raio_esfera ** 3

    if  vol_esfera  >  vol_balde :
      print ( 'O volume da esfera não cabe no balde' )
    mais :
      print ( 'O volume da esfera cabe no balde' )
  mais :
     print ( 'Medida Inadequada' )
    mais :
      print ( 'O volume da esfera cabe no balde' )
