""" 
A bit more polished animation script, showing how to do computation in a
background thread, and synchronize it with matplotlib output.

Try to understand what this does! You may wish to re-read it after the parallel
computation exercises.

"""

import time
import threading
import gobject

import numpy as np

import matplotlib
matplotlib.use('GTKAgg')
import matplotlib.pyplot as plt

from life import life_update

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
    gobject.threads_init()

    state = np.zeros((200, 300), dtype=np.int8)
    load_image(state, 'glider.png')

    # Prepare animation
    pixel_size = 2

    fig = plt.figure(dpi=50, figsize=(pixel_size * state.shape[1]/50., 
                                      pixel_size * state.shape[0]/50.))
    plt.axes([0, 0, 1, 1])
    img = plt.imshow(state, interpolation='nearest')
    plt.gray()

    manager = plt.get_current_fig_manager()
    animator = Animator(img, manager, state, framerate=30.0)
    animator.start()

    # Enter main loop
    plt.show()

    # Cleanup
    animator.stop()

class Animator:
    """
    Produce and draw a double-buffered animation, with computations in a
    separate thread

    Parameters
    ----------
    img
        Matplotlib imshow object to draw to
    manager
        Matplotlib figure manager
    state : ndarray
        Numpy array containing the initial simulation state
    framerate : float
        Frame rate of the simulation

    Attributes
    ----------
    img
        Matplotlib imshow object to draw to
    manager
        Matplotlib figure manager
    buffers : list of ndarrays
        List of two state buffers; buffers[1] is the new and buffers[0]
        the old state
    framerate : float
        Simulation framerate
    update_event : threading.Event
        Event signaling when to start computing the next frame,
        and whether the computation is finished
    stop_computation : bool
        Whether to exit all computation
    compute_thread : threading.Thread
        The thread doing the heavy lifting
    timeout_id : int
        GObject identifier for the timeout callback

    """

    def __init__(self, img, manager, state, framerate=2.0):
        self.img = img

        self.manager = manager
        self.buffers = [np.zeros_like(state), state]

        self.framerate = float(framerate)

        self.update_event = threading.Event()
        self.stop_computation = False

        self.compute_thread = threading.Thread(target=self.compute)

    def start(self):
        self.compute_thread.start()
        gobject.idle_add(self.draw_frame)

    def stop(self):
        self.stop_computation = True
        self.update_event.set()
        self.compute_thread.join()

    def compute(self):
        """Computation thread"""
        while not self.stop_computation:
            # Wait for a permission to render the next frame
            self.update_event.wait()

            # Render the next frame (let's hope it releases the GIL!!)
            life_update(self.buffers[0], self.buffers[1])

            # Signal that we finished redrawing the frame
            self.update_event.clear()

    def draw_frame(self, *args):
        """Draw a new frame. Called periodically every 1/framerate seconds."""

        start_time = time.time()

        if not self.stop_computation and not self.update_event.is_set():
            # Swap buffers
            self.buffers[:] = self.buffers[::-1]

            # Signal the compute thread that it can start computing the next
            # frame (goes into self.buffers[1])
            #
            # Note that above we check that the update_event is not set; the
            # compute thread clears the event after it has finished the
            # computation.
            self.update_event.set()

            # Draw onto screen.
            #
            # This in fact is the speed bottleneck!
            self.img.set_data(self.buffers[0])
            try:
                self.manager.canvas.draw()
            except AttributeError:
                # If the window is closed, the .canvas attribute seems to go
                # away, so catch that.
                return False

        end_time = time.time()
        rest_time = 1.0/self.framerate - (end_time - start_time)

        if rest_time < 0.010:
            # redrawing took too long: always wait at least 10 ms so
            # that the UI doesn't freeze up
            rest_time = 0.010

        # Re-queue
        gobject.timeout_add(
            int(1000*rest_time), # milliseconds
            self.draw_frame)

        # We re-schedule ourself manually
        return False

if __name__ == "__main__":
    main()

