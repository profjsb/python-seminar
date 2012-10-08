# There are plenty of ways of combining the different grey-level images into a
# false-color representation (it's a bit of an art!).  This is a very simple
# pipeline, that mainly tweaks intensities, and that does nothing fancy along
# the lines of denoising, sharpening, etc.

import numpy as np

from skimage import io
io.use_plugin('matplotlib')

from skimage import exposure

L = io.imread('m8_050507_9i9m_R_sm.png')
H = io.imread('m8_050507_9i9m_R_sm.png')
R = io.imread('m8_050507_9i9m_R_sm.png')
G = io.imread('m8_050507_9i9m_G_sm.png')
B = io.imread('m8_050507_9i9m_B_sm.png')

def gamma(img, g):
    return exposure.rescale_intensity(img ** g, in_range=(0, 1))

L = gamma(L, 0.8)
R = exposure.rescale_intensity(R + L, in_range=(0, 0.5))
G = exposure.rescale_intensity(G + L, in_range=(0, 0.4))
B = exposure.rescale_intensity(gamma(H, 1.5), in_range=(0, 0.03))

# Merge R, G, B, hydrogen and luminance
out = np.dstack((R, G, B))
out = exposure.rescale_intensity(gamma(out, 2), in_range=(0, 0.9))

io.imshow(out)
io.imsave('m8_recon.png', out)
io.show()
