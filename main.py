from codecs import backslashreplace_errors
import objeto
from math import dist
import matplotlib.pyplot as plt

pressionou = False

def gravidade(objeto1, objeto2):
    forca = (6.67 * (10**-11))*(objeto1.massa*objeto2.massa)/(dist((objeto1.x,objeto1.y),(objeto2.x,objeto2.y)))**2 
    return forca *-1

def colisao(objeto1,objeto2):
    if  objeto2.x <= objeto1.x + objeto1.raio <= objeto2.x + objeto2.raio:
        objeto1.parar()
    elif  objeto2.y <= objeto1.y + objeto1.raio <= objeto2.y + objeto2.raio:
        objeto1.parar()
    elif  objeto2.x >= objeto1.x - objeto1.raio >= objeto2.x - objeto2.raio:
        objeto1.parar()
    elif  objeto2.y >= objeto1.y - objeto1.raio >= objeto2.y - objeto2.raio:
        objeto1.parar()

terra = objeto.Objeto(0,0,2000000,0,0,0,0,10)
bala = objeto.Objeto(200,200,10,0,0,0,0,1)


for x in range(0,1000):
    forca = gravidade(bala,terra)
    bala.calcPos(forca)
    colisao(bala,terra)
    print("("+str(bala.x)+","+str(bala.y)+","+str(bala.velx)+","+str(bala.vely)+")")
    plt.xlim(0,1000)
    plt.ylim(0,1000)
    plt.scatter(terra.x,terra.y,color='blue')
    plt.scatter(bala.x,bala.y,color='black')
    plt.pause(0.001)
plt.show()




    

