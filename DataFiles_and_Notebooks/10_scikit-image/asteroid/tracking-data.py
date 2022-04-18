import numpy as np
import skimage as ski

M, N = 300, 400
frames = 10
stars = 500
sigma_scale = 1.2
noise_level = 0.1
object_sigma = 2

rng = np.random.default_rng()
img = np.zeros((M, N), dtype=float)

# Star positions and sigmas
positions = np.floor(rng.random((stars, 2)) * [M, N]).astype(int)
sigmas = rng.random(stars) * sigma_scale
brightness = rng.random(stars)

# Path
start = np.array([250, 20])
end = np.array([100, 370])

for i in range(stars):
    star_img = np.zeros((M, N), dtype=float)
    star_img[tuple(positions[i].T)] = brightness[i]
    star_img = ski.filters.gaussian(star_img, sigma=sigmas[i])
    img += star_img

all_images = []

for f in range(frames):
    frame_img = img.copy()

    # Add noise
    frame_img += rng.random((M, N)) * noise_level

    # Add object starting after reference frame
    if f > 0:
        # Position of object
        pos = np.floor(start + (end - start) / frames * (f - 1)).astype(int)
        print(pos)

        obj = np.zeros_like(img)
        obj[tuple(pos.T)] = 3
        obj = ski.filters.gaussian(obj, 1.5)

        frame_img += obj

    frame_img = np.clip(frame_img, 0, 1)

    all_images.append(frame_img)

#    import matplotlib.pyplot as plt
#    plt.imshow(frame_img, cmap='gray')
#    plt.show()

#plt.imshow(all_images[2] - all_images[0], cmap='gray')
#plt.show()

for i in range(len(all_images)):
    print(f'Saving image {i}...')
    ski.io.imsave(f'asteroid_{i:03d}.png', all_images[i])
