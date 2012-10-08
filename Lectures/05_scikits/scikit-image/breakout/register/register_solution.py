from skimage import io, transform

import numpy as np
import matplotlib.pyplot as plt
import os


# Load the two landscape photos
img0 = io.imread('webreg_0.jpg')
img1 = io.imread('webreg_1.jpg')


def choose_corresponding_points():
    """Utility function for finding corresponding features in images.

    Alternately click on image 0 and 1, indicating the same feature.

    """
    f, (ax0, ax1) = plt.subplots(1, 2)
    ax0.imshow(img0)
    ax1.imshow(img1)

    coords = plt.ginput(8, timeout=0)

    np.savez('_reg_coords.npz', source=coords[::2], target=coords[1::2])

    plt.close()


# Re use previous coordinates, if found
if not os.path.exists('_reg_coords.npz'):
    choose_corresponding_points()

coords = np.load('_reg_coords.npz')

# Estimate the transformation between the two sets of coordinates,
# assuming it is an affine transform
tf = transform.estimate_transform('affine', coords['source'], coords['target'])

# Use a translation transformation to center both images for display purposes
offset = transform.AffineTransform(translation=(-200, -170))

img0_warped = transform.warp(img0, inverse_map=offset,
                             output_shape=(600, 600))

img1_warped = transform.warp(img1, inverse_map=offset + tf,
                             output_shape=(600, 600))


# Find where both images overlap; in that region average their values
mask = (img0_warped != 0) & (img1_warped != 0)
registered = img0_warped + img1_warped
registered[mask] /= 2

# Display the results
f, (ax0, ax1, ax2) = plt.subplots(1, 3, subplot_kw={'xticks': [], 'yticks': []})
ax0.imshow(img0)
ax1.imshow(img1)
ax2.imshow(registered)

## ## Display image boundaries
## y, x = img1.shape[:2]
## box = np.array([[0, 0], [0, y], [x, y], [x, 0], [0, 0]])
## tf_box = (offset + tf).inverse(box)
## plt.plot(tf_box[:, 0], tf_box[:, 1], 'r-')

plt.show()
