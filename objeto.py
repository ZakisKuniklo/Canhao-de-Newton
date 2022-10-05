import math
class Objeto():

    def __init__(self,x,y,massa,velx,vely,accx,accy,raio):
        self.x = x
        self.y = y
        self.massa = massa
        self.velx = velx
        self.vely = vely
        self.accx = accx
        self.accy = accy
        self.raio = raio
    
    def calcPos(self,forca):
        self.x = self.x + self.velx
        self.y = self.y + self.vely
        self.calcVel(forca)
    
    def calcVel(self,forca):
        self.velx = self.velx + self.accx
        self.vely = self.vely + self.accy
        self.calcAcc(forca)
    
    def calcAcc(self,forca):
        aceleracao = forca/self.massa
        coefAng = self.x-0/self.y-0
        angulo = math.atan(coefAng)
        self.accx = math.cos(angulo) * aceleracao
        self.accy = math.sin(angulo) * aceleracao
    
    def parar(self):
        self.velx = 0
        self.vely = 0
        self.accx = 0
        self.accy = 0