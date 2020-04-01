from PIL import Image
import numpy as np


def composite(dval1, dval2):
    mountimg = Image.open('d:/Screenshots/Emily/diffD pairs/Mountains/s' + str(mtnSeedNum) + '_d' + dval1 + '.png').convert("RGBA")  # Mountain Image
    cloudimg = Image.open('d:/Screenshots/Emily/diffD pairs/Clouds/s' + str(cloudSeedNum) + '_d' + dval2 + '.png').convert("RGBA")  # Cloud Image

    data = np.array(cloudimg)  # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T  # Temporarily unpack the channels for readability
    blackarea = (red == 0) & (blue == 0) & (green == 0)  # Define black area
    data[..., :-1][blackarea.T] = (200, 200, 200)  # Change black area to grey

    greyclouds = Image.fromarray(data)
    red, green, blue, alpha = mountimg.split()  # Make channels viable for mask

    comp = Image.composite(greyclouds, mountimg, green)

    #comp.show()

    comp.save(r'd:\screenshots\_Fractal Soup Stimuli\4_diffD_combos\seed' + str(mtnSeedNum) + '_' + str(cloudSeedNum) + '_D' + str(x) + '_' + str(y) + '.png', 'PNG')


# Combos are stored in two lists:
list1 = [1.1, 1.1, 1.1, 1.1, 1.3, 1.3, 1.3, 1.3, 1.5, 1.5, 1.5, 1.5, 1.7, 1.7, 1.7, 1.7, 1.9, 1.9, 1.9, 1.9,
         1.1, 1.1, 1.1, 1.1, 1.3, 1.3, 1.3, 1.3, 1.5, 1.5, 1.5, 1.5, 1.7, 1.7, 1.7, 1.7, 1.9, 1.9, 1.9, 1.9]
list2 = [1.3, 1.5, 1.7, 1.9, 1.1, 1.5, 1.7, 1.9, 1.1, 1.3, 1.7, 1.9, 1.1, 1.3, 1.5, 1.9, 1.1, 1.3, 1.5, 1.7,
         1.3, 1.5, 1.7, 1.9, 1.1, 1.5, 1.7, 1.9, 1.1, 1.3, 1.7, 1.9, 1.1, 1.3, 1.5, 1.9, 1.1, 1.3, 1.5, 1.7]

mtnSeedNum = -1
cloudSeedNum = 0

for x, y in zip(list1, list2):
    mtnSeedNum += 2
    cloudSeedNum += 2
    print('seed'+str(mtnSeedNum)+'/'+str(cloudSeedNum))
    print(str(x) + ',' + str(y))

    composite(str(x), str(y))  # Run composite function
