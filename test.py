# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#filename = '/home/aifa/timg.jpeg'
filename = '/home/aifa/timg-1.jpeg'
#filename = '/home/aifa/timg-2.jpeg'

im=Image.open( filename )
print (im.format, im.size, im.mode)

im.show()

image = np.array(im)

print 'show original image..'
print image.shape

#im.show()
#image

# show
plt.imshow(image)
plt.show()


# vertical reverse
print 'vertical reverse'
plt.imshow(image[-1::-1,:,:] )
plt.show()

# horizontal reverse
print 'horizontal reverse'
plt.imshow(image[:,-1::-1,:] )
plt.show()

# rgb reverse
print 'rgb reverse'
plt.imshow(image[:,:,-1::-1] )
plt.show()

width=image.shape[0]
height=image.shape[1]
rgb=image.shape[2]

cx= width/2
cy= height/2

# clip a quarter of the image - topleft
print 'clip a quarter of the image - topleft'
plt.imshow(image[:cx ,:cy, :] )
plt.show()

# clip a quarter of the image - topright
print 'clip a quarter of the image - topright'
plt.imshow(image[:cx ,cy:-1, :] )
plt.show()

# hotrizontal reverse and only take 1/5 
print 'hotrizontal reverse and only take 1/5 '
plt.imshow(image[:cx:5 ,cy:0:-5, :] )
plt.show()

# clip a quarter of the image - topleft, horizontal reverse, reverse colors
print 'clip a quarter of the image - topleft, horizontal reverse, reverse colors'
image1 = image.copy()
image1 = 255 - image[:cx: ,cy:0:-1, :]
plt.imshow(image1)
plt.show()

# reverse only red tunnel color
print 'reverse only red tunnel color'
image2 = image.copy()
image2[:,:,0:1] = 255-image2[:,:,0:1]
plt.imshow(image2)
plt.show()

# reverse rgb order 
print 'reverse rgb order '
image3 = image.copy()
image3[:,:,:] = image3[:,:,-1::-1]
plt.imshow(image3)
plt.show()

# reverse rgb order, only take 1/5
print 'reverse rgb order, only take 1/5'
image4 = image.copy()
image4 = image4[::5,::5,-1::-1]
plt.imshow(image4)
plt.show()


# mosaic by 16-pixel block
print 'mosaic all image by 16-pixel block'
image5 = image.copy()
mosaic_size=22

for h in np.arange(0, width, mosaic_size):
    for v in np.arange(0, height, mosaic_size):
        image5[h:h+mosaic_size, v:v+mosaic_size, :] = image5[h][v][:]
        #image5[h:h+mosaic_size, v:v+mosaic_size, :] = image5[h+mosaic_size/2][v+mosaic_size/2][:]
        
plt.imshow(image5)
plt.show()

# color multiply - overload is not considered        
#image6 = image * 4
#plt.imshow(image6)
#plt.show()

# define a circle clip region
alpha = np.arange(0, 360, 1)
r = 200
rad = alpha * np.pi / 180
x = r * np.cos(rad)
y = r * np.sin(rad)

x = x.astype('int')
y = y.astype('int')

x += 300
y += 400

# mosaic a round regrion by 16-pixel block with radius 200
print 'mosaic a round regrion by 16-pixel block with radius 200'
image7 = image.copy()

for h in np.arange(0, width, mosaic_size):
    for v in np.arange(0, height, mosaic_size):
        #if v > min(x) and v < max(x) \
        #and h > min(y) and h < max(y):
            #image7[h:h+mosaic_size, v:v+mosaic_size, :] = image7[h][v][:]
        if np.power(v-cy, 2) + np.power(h-cx, 2) < np.power(r, 2):      # check the distance to point (cx, cy)
            image7[h:h+mosaic_size, v:v+mosaic_size,:] = image7[h+mosaic_size/2][v+mosaic_size/2][:]

plt.imshow(image7)
plt.show()










GIT-CONFIG(1)                                                                                 Git Manual                                                                                 GIT-CONFIG(1)

NAME
       git-config - Get and set repository or global options

SYNOPSIS
       git config [<file-option>] [type] [-z|--null] name [value [value_regex]]
       git config [<file-option>] [type] --add name value
       git config [<file-option>] [type] --replace-all name value [value_regex]
       git config [<file-option>] [type] [-z|--null] --get name [value_regex]
hahahahaha
#uuuuuuuu
