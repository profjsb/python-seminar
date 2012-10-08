from skimage import data, transform

import numpy as np
import matplotlib.pyplot as plt



image = data.text()

plt.imshow(image, cmap=plt.cm.gray)

target = np.array(plt.ginput(4))
source = np.array([(0, 0), (0, 50), (300, 50), (300, 0)])

plt.close()

pt = transform.ProjectiveTransform()
pt.estimate(source, target)

warped = transform.warp(image, pt, output_shape=(50, 300))



f, (ax0, ax1) = plt.subplots(1, 2)
ax0.imshow(image, cmap=plt.cm.gray)
ax1.imshow(warped, cmap=plt.cm.gray)
plt.show()
