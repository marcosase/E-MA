'''
Created on Apr 30, 2019

@author: rodrigo.guercio
'''
import imageio


if __name__ == '__main__':
  
  
    PATH = '/home/ABTLUS/rodrigo.guercio/Desktop/'
    filename = 'lab6_3p20GPa_300K_300s_n001.tiff'
    #filename = 'Setup-Uniformidade.jpg'
    msg =  PATH + filename
    ima = imageio.imread(msg)
    print(ima.shape)
    print(ima[3,4])
    print(ima)
    a = (ima + ima+ 0)+100
    print(a) 
    print(type(ima))
    print(type(a))
    #imageio.imwrite(uri = PATH + 'aa.tiff', im = a)