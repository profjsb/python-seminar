# Run this file with
#
#     python run_life.py -dGTKAgg
#

import numpy as np
from matplotlib import pyplot as plt, animation

from life import life_update
import time


def load_image(state, file_name):
    img = plt.imread(file_name)

    w = img.shape[0]
    h = img.shape[1]

    cx = state.shape[0]//2
    cy = state.shape[1]//2

    x0 = cx - w//2
    y0 = cy - h//2

    state[x0:x0+w, y0:y0+h] = img


def main():
    global state_1, state_2

    state_1 = np.zeros((200, 300), dtype=np.intc)
    state_2 = np.zeros((200, 300), dtype=np.intc)

    load_image(state_1, 'breeder.png')

    # Prepare animation
    pixel_size = 2

    fig = plt.figure(dpi=50, figsize=(pixel_size * state_1.shape[1]/50.,
                                      pixel_size * state_2.shape[0]/50.))
    plt.axes([0, 0, 1, 1])
    img = plt.imshow(state_1, interpolation='nearest',
                              cmap=plt.cm.gray)

    print "Press Ctrl-C in the terminal to exit..."

    def update_fig(n):
        global state_1, state_2

        life_update(state_1, state_2)
        state_1, state_2 = state_2, state_1   # swap buffers

        img.set_array(state_1)

        return img,

    ani = animation.FuncAnimation(fig, update_fig, interval=50, blit=True)
    plt.show()


if __name__ == "__main__":
    main()
