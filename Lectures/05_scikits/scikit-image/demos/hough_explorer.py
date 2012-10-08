import matplotlib.collections as mcoll

from skimage import data
from skimage.filter import canny
from skimage.transform import probabilistic_hough

from skimage.viewer import ImageViewer
from skimage.viewer.widgets import Slider
from skimage.viewer.plugins.overlayplugin import OverlayPlugin


class HoughPlugin(OverlayPlugin):

    def image_filter(self, image, **kwargs):
        canny_keys = ('sigma', 'low_threshold', 'high_threshold')
        canny_kwargs = dict([(k, kwargs.pop(k)) for k in canny_keys])
        hough_kwargs = kwargs
        edges = canny(image, **canny_kwargs)
        lines = probabilistic_hough(edges, **hough_kwargs)
        self._lines = lines
        return edges

    def display_filtered_image(self, edges):
        self.overlay = edges
        if hasattr(self, '_hough_lines'):
            self.image_viewer.ax.collections.remove(self._hough_lines)
        self._hough_lines = mcoll.LineCollection(self._lines, colors='r')
        self.image_viewer.ax.add_collection(self._hough_lines)
        self.image_viewer.redraw()

image = data.text()

# Note: ImageViewer must be called before Plugin b/c it starts the event loop.
viewer = ImageViewer(image)
# You can create a UI for a filter just by passing a filter function...
plugin = HoughPlugin()
plugin += Slider('sigma', 0, 5, value=1, update_on='release')
plugin += Slider('low threshold', 0, 255, update_on='release')
plugin += Slider('high threshold', 0, 255, update_on='release')
plugin += Slider('threshold', 0, 255, update_on='release')
plugin += Slider('line length', 0, 100, update_on='release')
plugin += Slider('line gap', 0, 20, update_on='release')
# Finally, attach the plugin to the image viewer.
viewer += plugin
viewer.show()
