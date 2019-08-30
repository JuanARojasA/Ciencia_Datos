import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from scipy import misc

#Funcion Escala de Grises
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def masc(img):
    imgfilt = np.zeros((img.shape[0],img.shape[1]))
    img = np.pad(img, 1, mode='wrap')

    for y in range(1,img.shape[0]-1):
        for x in range(1,img.shape[1]-1):
            imgfilt[y-1,x-1]=np.sum(np.multiply(f,img[y-1:y+2,x-1:x+2]))
            
    misc.imsave('facefiltro.png', imgfilt)
    #plt.imshow(imgfilt, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    #plt.show()
    return imgfilt
    

#Cargar la Imagen de la libreria Scypy
img = misc.face()
misc.imsave('face.png', img)
plt.imshow(img)
plt.show()

#Convertir la Imagen a escala de grises
img = mpimg.imread('face.png')  
img = rgb2gray(img)
misc.imsave('facegray.png', img)
plt.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()

#Filtro
f = np.full((3,3),1/9)

#Aplicar Suavizado
for i in range(100):
    img = masc(img)
    print(i)
    