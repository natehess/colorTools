from PIL import Image
import numpy as np


def composite(dval1, dval2):
    mountimg = Image.open('mountainExample' + dval1 + '.png').convert("RGBA")  # Mountain Image
    cloudimg = Image.open('cloudExample' + dval2 + '.png').convert("RGBA")  # Cloud Image

    data = np.array(cloudimg)  # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T  # Temporarily unpack the channels for readability
    blackarea = (red == 0) & (blue == 0) & (green == 0)  # Pull out black areas
    data[..., :-1][blackarea.T] = (200, 200, 200)  # Transpose black to grey

    grayclouds = Image.fromarray(data)
    red, green, blue, alpha = mountimg.split()  #

    comp = Image.composite(grayclouds, mountimg, green)

    comp.show()

    comp.save(r'd:\IPL_PycharmProjects\colorSwitchers\compTest' + str(x) + '_' + str(y) + '.png', 'PNG')


list1 = [1, 1, 1]
list2 = [1, 1, 1]
seedNum = 0

for x, y in zip(list1, list2):
    seedNum += 1
    print('seed'+str(seedNum))
    print(str(x) + ',' + str(y))

    composite(str(x), str(y))
