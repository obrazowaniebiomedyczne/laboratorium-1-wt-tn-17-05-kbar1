
"""
Rozwiązania do laboratorium 1 z Obrazowania Biomedycznego.
"""
import numpy as np

"""
3 - Kwadrat
"""
def square(size, side, start):
    image = np.zeros((size, size)).astype(np.uint8)
    image[start[1]:start[1]+side,start[0]:start[0]+side] = 255
    return image

"""
3 - Koło
"""
def midcircle(size):
    y0 = size[0]/2
    x0 = size[1]/2

    if y0<x0:
    	r = y0/2
    else:
    	r = x0/2

    image = np.zeros((size[0],size[1])).astype(np.uint8)
    y,x = np.ogrid[0:size[0], 0:size[1]]
    mask = ((x-x0)**2 + (y-y0)**2) < r**2
    image[mask] = 255
    return image

"""
3 - Szachownica.
"""
def checkerboard(size):
    image = np.zeros((size,size)).astype(np.uint8)
    side = int(size/8)
    counter = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if ((i+j) % 2 == 1):
                counter = counter + 1
                image[i*side:i*side + side,
                j*side:j*side + side] = 255
    return image
"""
4 - Interpolacja najbliższych sąsiadów.
"""
def nn_interpolation(source, new_size):
    #lenna = read_png('data/mono/lenna.png')
    #lenna = np.squeeze(lenna)
    pass


"""
5 - Interpolacja dwuliniowa
"""
def bilinear_interpolation(source, new_size):
    pass
