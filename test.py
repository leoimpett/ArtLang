from bokeh.models import Select
from bokeh.layouts import row, widgetbox
from bokeh.plotting import curdoc, figure
from bokeh.models import CustomJS, ColumnDataSource, Slider
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import skimage.transform as trs
import skimage.color as sColor
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool

from datastruct.imagedata import *

data= {"x_tsne":[1,2,3,4,5],"y_tsne":[2,3,5,4,8],"hue":[2,2,3,8,7],"sat":[5,8,1,2,3]}
data=pd.DataFrame(data=data)
columns = sorted(data.columns)

def create_figure():
    xs = data[x.value].values
    ys = data[y.value].values
    x_title = x.value.title()
    y_title = y.value.title()
    kw = {
        
    }
    kw['title'] = "%s vs %s" % (x_title, y_title)

    p = figure(plot_height=600, plot_width=800, tools='pan,box_zoom,hover,reset', **kw)
    p.xaxis.axis_label = x_title
    p.yaxis.axis_label = y_title

    #p.image(image = images.extract_lowRes()[:5],x=xs, y=ys, dw=32,dh=32)
    p.circle(x=xs, y=ys, size=35)

    return p

def update(attr, old, new):
    layout.children[1] = create_figure()
    
output_file("test.html")


columns = sorted(data.columns)

x = Select(title='X-Axis', value='hue', options=columns)
x.on_change('value', update)

y = Select(title='Y-Axis', value='sat', options=columns)
y.on_change('value', update)


controls = widgetbox([x, y], width=200)
layout = row(controls, create_figure())

curdoc().add_root(layout)

curdoc().title = "test"
