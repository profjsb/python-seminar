# There are plenty of ways of combining the different grey-level images into a
# false-color representation (it's a bit of an art!).  This is a very simple
# pipeline, that mainly tweaks intensities, and that does nothing fancy along
# the lines of denoising, sharpening, etc.

import numpy as np
import matplotlib.pyplot as plt

from skimage import img_as_float, io, exposure

ic = io.ImageCollection('m8_050507_*.png')
ic = [img_as_float(img) for img in ic]
H, B, G, R, L = ic

H = exposure.adjust_sigmoid(H, cutoff=0.05, gain=35)
L = exposure.adjust_sigmoid(L, cutoff=0.05, gain=15)
R = exposure.adjust_gamma(R, 0.1)

# Merge R, G, B channels
out = np.dstack((H, L, R))
out = exposure.adjust_gamma(out, 2.1)

io.imsave('m8_recon.png', out)

f, ax = plt.subplots()
ax.imshow(out)
plt.show()
