from PIL import Image
import numpy as np



baseImg = Image.open('mfTest1.png')
baseImg = baseImg.convert('RGBA')

data = np.array(baseImg)   # "data" is a height x width x 4 numpy array
red, green, blue, alpha = data.T # Temporarily unpack the bands for readability

# Replace white with red... (leaves alpha values alone...)
whiteArea = (red == 255) & (blue == 255) & (green == 255)
greyArea = (red == 201) & (blue == 201) & (green == 201)
blackArea = (red == 0) & (blue == 0) & (green == 0)

r = 128
g = 255
b = 0

toggleRed = 0
toggleGreen = 1
toggleBlue = 0

for i in range(1000):
    if toggleRed == 0:
        r += 1
    else:
        r -= 1
    if toggleGreen == 0:
        g += 1
    else:
        g -= 1
    if toggleBlue == 0:
        b += 1
    else:
        b -= 1
    data[..., :-1][whiteArea.T] = (r, r, r)  # Transpose back needed
    data[..., :-1][blackArea.T] = (g, g, g)  # Transpose back needed
    data[..., :-1][greyArea.T] = (b, b, b)  # Transpose back needed
    print(r, b, g)
    im2 = Image.fromarray(data)
    im2.save(r'd:\IPL_PycharmProjects\test'+str(i)+'.png', 'PNG')
    #  Limit Switches
    if r >= 255:
        toggleRed = 1
    if r <= 0:
        toggleRed = 0
    if g >= 255:
        toggleGreen = 1
    if g <= 0:
        toggleGreen = 0
    if b >= 255:
        toggleBlue = 1
    if b <= 0:
        toggleBlue = 0


