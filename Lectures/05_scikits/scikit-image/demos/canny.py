from skimage.viewer import ImageViewer
from skimage.viewer.widgets import Slider
from skimage.viewer.plugins.overlayplugin import OverlayPlugin

from skimage import data, filter

image = data.coins()

viewer = ImageViewer(image)

plugin = OverlayPlugin(image_filter=filter.canny)
plugin += Slider('sigma', 0, 5, update_on='release')
viewer += plugin

viewer.show()
