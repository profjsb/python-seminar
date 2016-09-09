
"""
live streaming example from a BBC microbit

UC Berkeley Python Seminar
"""
from numpy.random import uniform

from bokeh.layouts import row, column, gridplot
from bokeh.models import ColumnDataSource, Slider, Select, Range1d
from bokeh.plotting import curdoc, figure
from bokeh.driving import count

import serial
ser = serial.Serial('/dev/cu.usbmodem1422',115200)

BUFSIZE = 30

source = ColumnDataSource(dict(
    time=[], x=[], y=[], z=[], l=[]
))

p = figure(plot_height=500, tools="xpan,xwheel_zoom,xbox_zoom,reset", y_axis_location="right")

p.x_range.follow = "end"
p.x_range.follow_interval = 100
p.x_range.range_padding = 0
p.xaxis.axis_label = "time"
p.yaxis.axis_label = "accel [mg]"
p.axis.axis_label_text_font_style = "bold"
#p.y_range = Range1d(-2000,2000)


p.line(x='time', y='z', alpha=0.2, line_width=3, color='red', source=source,legend="z")
p.line(x='time', y='x', alpha=0.2, line_width=3, color='navy', source=source,legend="x")
p.line(x='time', y='y', alpha=0.2, line_width=3, color='green', source=source,legend="y")

p2 = figure(plot_height=250, x_range=p.x_range, tools="xpan,xwheel_zoom,xbox_zoom,reset", y_axis_location="right")
p2.line(x='time', y='l', color='purple', source=source)
p2.xaxis.axis_label = "time"
p2.yaxis.axis_label = "light level"
p2.axis.axis_label_text_font_style = "bold"

curdoc().add_root(gridplot([[p], [p2]], toolbar_location="left", plot_width=1000))


@count()
def update(t):
    #print("here")
    new_vals = ser.readlines(50)
    #print(new_vals)
    gotz = False
    tt = None
    z = None
    for v in new_vals:
        if str(v).find("z:") != -1:
            gotz = True
            z=int(str(v.strip()).split(":")[1].replace("'",""))
            #print("z",z)
        if str(v).find("y:") != -1 and gotz:
            y=int(str(v.strip()).split(":")[1].replace("'",""))
            #print("y",y)
        if str(v).find("x:") != -1 and gotz:
            x=int(str(v.strip()).split(":")[1].replace("'",""))
            #print("x",x)
        if str(v).find("l:") != -1 and gotz:
            l=int(str(v.strip()).split(":")[1].replace("'",""))
            #print("l",l)
        if str(v).find("t:") != -1 and gotz:
            tt=int(str(v.strip()).split(":")[1].replace("'",""))/1000.
            #print("tt",tt/100.)
            break

    if v is None or tt is None:
        return

    new_data = dict(
        time=[tt],
        z=[z], y=[y], x=[x], l=[l]
    )

    source.stream(new_data, 300)

curdoc().add_periodic_callback(update, 50)
curdoc().title = "Acceleration/Microbit"
