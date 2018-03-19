# Josh Bloom
# adapted from https://gist.github.com/craffel/2d727968c3aaebd10359
# added plotter for sklearn CLF

import matplotlib.pyplot as plt
import math

def draw_MLP_model(ax,clf,left=0.1, right=0.9, bottom=0.1, top=0.9):
    '''
    input a trained clf
    '''
    input_num = (clf.coefs_[0].shape[0],)
    output_num = (clf.coefs_[-1].shape[1],)
    structure = input_num + clf.hidden_layer_sizes + output_num

    return draw_neural_net(ax,left, right, bottom, top,structure,weights=clf.coefs_)

def draw_neural_net(ax, left, right, bottom, top, layer_sizes,weights=None):
    '''
    Draw a neural network cartoon using matplotilb.
    
    :usage:
        >>> fig = plt.figure(figsize=(12, 12))
        >>> ax = fig.gca()
        >>> ax.axis('off')
        >>> draw_neural_net(fig.gca(), .1, .9, .1, .9, [4, 7, 2])
        >>> fig.savefig('nn.png')
    
    :parameters:
        - ax : matplotlib.axes.AxesSubplot
            The axes on which to plot the cartoon (get e.g. by plt.gca())
        - left : float
            The center of the leftmost node(s) will be placed here
        - right : float
            The center of the rightmost node(s) will be placed here
        - bottom : float
            The center of the bottommost node(s) will be placed here
        - top : float
            The center of the topmost node(s) will be placed here
        - layer_sizes : list of int
            List of layer sizes, including input and output dimensionality
    '''
    n_layers = len(layer_sizes)
    v_spacing = (top - bottom)/float(max(layer_sizes))
    h_spacing = (right - left)/float(len(layer_sizes) - 1)

    # Nodes
    for n, layer_size in enumerate(layer_sizes):
        layer_top = v_spacing*(layer_size - 1)/2. + (top + bottom)/2.
        for j,m in enumerate(range(layer_size)):
            circle = plt.Circle((n*h_spacing + left, layer_top - m*v_spacing), v_spacing/4.,
                                color='w', ec='k', zorder=4,linewidth=1)
            ax.add_artist(circle)

            x1,y1 = (n*h_spacing + left - v_spacing/8., layer_top - m*v_spacing -  v_spacing/32.)
            if n == 0:
                ## input labels
                txt = plt.Text(x1,y1,r"$X_i^{" + r"{}".format(j) + r"}$",zorder=10,fontsize=15)
                ax.add_artist(txt)

            if n == len(layer_sizes) - 1:
                txt = plt.Text(x1,y1,r"$Y_i^{" + r"{}".format(j) + r"}$",zorder=10,fontsize=15)
                ax.add_artist(txt)

    # Edges
    for n, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
        layer_top_a = v_spacing*(layer_size_a - 1)/2. + (top + bottom)/2.
        layer_top_b = v_spacing*(layer_size_b - 1)/2. + (top + bottom)/2.
        for j,m in enumerate(range(layer_size_a)):
            for k,o in enumerate(range(layer_size_b)):
                line = plt.Line2D([n*h_spacing + left, (n + 1)*h_spacing + left],
                                  [layer_top_a - m*v_spacing, layer_top_b - o*v_spacing], 
                                  linewidth=1, c='grey')
                ax.add_artist(line)
                if weights:
                    slope = ((layer_top_a - m*v_spacing) - (layer_top_b - o*v_spacing)) / \
                            ((n*h_spacing + left) - ((n + 1)*h_spacing + left))
                    slope_ang = math.atan2((layer_top_a - m*v_spacing) - (layer_top_b - o*v_spacing),\
                                          (n*h_spacing + left) - ((n + 1)*h_spacing + left))
                    intercept = (layer_top_a - m*v_spacing) - slope*(n*h_spacing + left)
                    x = (n + 1)*h_spacing + left + math.sqrt((0.55/layer_size_b))*((n*h_spacing + left) - ((n + 1)*h_spacing + left))
                    y = slope*x + intercept
                    ax.text(x,y,"%0.2f" % weights[n][j][k],rotation=(slope_ang + math.pi)*180/math.pi,
                            color="grey",alpha=0.9,fontsize=15)

