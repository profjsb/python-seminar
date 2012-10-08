from skimage import graph, color

bh = io.imread('borehole_stringer.png')

p, cost = graph.shortest_path(color.rgb2grey(bh), reach=1)

plt.imshow(bh, cmap=plt.cm.gray)
plt.plot(np.arange(bh.shape[1]), p, 'r-');

