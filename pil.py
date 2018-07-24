from __future__ import print_function
import os
import sys
from PIL import Image, ImageSequence

infile = 'superman.gif'
output = 'frame'
im = Image.open(infile)

frames = sum(1 for _ in ImageSequence.Iterator(im))
print(frames,'frames')
divisiones = round(im.size[0]/frames)
ancho_start = 0
ancho_end = divisiones


count = 0

def moireiser(imagen, start, ancho, ):
    box = (start, 0, ancho, imagen.size[1])
    print(box,'box',start,'start',ancho_end,'row')
    cropped_image = im.crop(box)
    cropped_image.save('./frames/'+output+str(count)+'.gif')
    print('se guardo')

for f in ImageSequence.Iterator(im):
    count+=1
    ancho_start = ancho_end
    ancho_end += divisiones
    moireiser(im,ancho_start,ancho_end)
