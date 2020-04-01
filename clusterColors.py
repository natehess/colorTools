from matplotlib import pyplot as plt
from matplotlib import image as img
from scipy.cluster.vq import kmeans
from scipy.cluster.vq import whiten
import pandas as pd

image = img.imread('./images/allColors1k.jpg')

r = []
g = []
b = []
for line in image:
    for pixel in line:
        temp_r, temp_g, temp_b = pixel
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)

df = pd.DataFrame({'red': r, 'blue': b, 'green': g})

df['scaled_red'] = whiten(df['red'])
df['scaled_blue'] = whiten(df['blue'])
df['scaled_green'] = whiten(df['green'])
df.sample(n = 10)

print(df)

cluster_centers, distortion = kmeans(df[['scaled_red', 'scaled_green', 'scaled_blue']], 2)

colors = []
r_std, g_std, b_std = df[['red', 'green', 'blue']].std()

for cluster_center in cluster_centers:
    scaled_r, scaled_g, scaled_b = cluster_center
    colors.append((
        scaled_r * r_std / 255,
        scaled_g * g_std / 255,
        scaled_b * b_std / 255
        ))

plt.imshow([colors])
plt.show()
