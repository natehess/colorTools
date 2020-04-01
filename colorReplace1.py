from PIL import Image
import numpy as np

im = Image.open('mfTest1.png')
im = im.convert('RGBA')

data = np.array(im)   # "data" is a height x width x 4 numpy array
red, green, blue, alpha = data.T # Temporarily unpack the bands for readability

# Replace white with red... (leaves alpha values alone...)
whiteArea = (red == 255) & (blue == 255) & (green == 255)
greyArea = (red == 201) & (blue == 201) & (green == 201)
blackArea = (red == 0) & (blue == 0) & (green == 0)

data[..., :-1][whiteArea.T] = (255, 0, 0) # Transpose back needed
data[..., :-1][greyArea.T] = (0, 255, 0) # Transpose back needed
data[..., :-1][blackArea.T] = (0, 0, 255) # Transpose back needed

im2 = Image.fromarray(data)
im2.show()



