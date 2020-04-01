from PIL import Image
import numpy as np

mountImg = Image.open('mountainExample.png').convert("RGBA")  # Mountain Image
cloudImg = Image.open('cloudExample.png').convert("RGBA")  # Cloud Image
#  mask = Image.new("L", mountImg.size, 128)  # Generated gray mask

data = np.array(cloudImg)  # "data" is a height x width x 4 numpy array
red, green, blue, alpha = data.T  # Temporarily unpack the channels for readability
blackArea = (red == 0) & (blue == 0) & (green == 0)  # Pull out black areas
data[..., :-1][blackArea.T] = (200, 200, 200)  # Transpose black to grey

grayClouds = Image.fromarray(data)
red, green, blue, alpha = mountImg.split()  #

comp = Image.composite(grayClouds, mountImg, green)

comp.show()

comp.save(r'd:\IPL_PycharmProjects\colorSwitchers\compTest.png', 'PNG')

# try defining a function where there are 2 args that coresspond to D values in the image titles