import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from scipy import misc

#Funcion Escala de Grises
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def serieAleatoria():
    a = np.arange(16)
    np.random.shuffle(a)
    print(a)
    return a

def posMatx(id):
    pos = [id//4,id%4]
    return pos

def Intercambio(img):
    ySize = img.shape[0]//4
    xSize = img.shape[1]//4
    
    nuevaPos = serieAleatoria()
    imgChg = np.zeros((ySize*4,xSize*4))
    for i in range(len(nuevaPos)):
        posChg = posMatx(i)
        posOrg = posMatx(nuevaPos[i])
        imgChg[posChg[0]*ySize:(posChg[0]*ySize)+ySize, posChg[1]*xSize:(posChg[1]*xSize)+xSize] = img[posOrg[0]*ySize:(posOrg[0]*ySize)+ySize, posOrg[1]*xSize:(posOrg[1]*xSize)+xSize]
    misc.imsave('imgChg.png', imgChg)
    plt.imshow(imgChg, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    plt.show()

img = misc.face()
misc.imsave('img.png', img)
plt.imshow(img)
plt.show()

#Convertir la Imagen a escala de grises
img = mpimg.imread('img.png')  
img = rgb2gray(img)
misc.imsave('imgGray.png', img)
plt.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()

Intercambio(img)