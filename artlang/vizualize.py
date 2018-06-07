from matplotlib.offsetbox import AnnotationBbox,OffsetImage
import numpy as np
import matplotlib.pyplot as plt
import easygui
import skimage.color as sColor
from bokeh.plotting import figure, show, output_notebook,output_file,ColumnDataSource
from bokeh.models import HoverTool



#PLot a set of images with respect to the x and y coordinates given in parameter
def plot_xy_and_save(xy,imagesData,show_notebook=True):
    images = imagesData.extract_lowRes()
    fig = plt.figure(figsize=(170, 170))
    plt.scatter(xy[:, 0], xy[:, 1], marker=None)

    ax = plt.subplot(111)
    
    for i in range(len(images)) :
        im = OffsetImage(images[i], cmap = 'gray', zoom=0.70)
        im.image.axis =ax
        ab =AnnotationBbox(im,[xy[i,0],xy[i,1]],frameon=False) 
        ax.add_artist(ab)
    if(not show_notebook):
        filename = easygui.filesavebox(msg = "Give a name to your plot")
        fig.savefig(filename + ".jpg")
        
    else:
        plt.show()

    
#PLot a set of images with respect to the x and y coordinates, and using the interactive plot tool bokeh to ba able to display additionnal data
#Datas are only the names of the data the user wants in the bokeh plot as they are nammed in the collection (e.g. date, hue, etc...)
def bokeh_plot(imagesData,datas,xy):
    
    #Converting to greyscale to get bokeh support
    grey = []
    squaredImg = imagesData.extract_lowRes()
    for img in squaredImg :
        grey.append(sColor.rgb2gray(np.flipud(img)))
    
        
    filename = easygui.filesavebox(msg = "Give a name to your plot")
    output_file(filename + ".html")
     
    #Creating the basic and the enhanced dictionnaries for each datas asked
    values = []
    for elem in datas:
        values.append(imageData.get_data_forall(elem))
    mydict={}
    for i in range(len(datas)):
        mydict[datas[i]] = values[i]
    
    xandy = dict(
        image= grey,
        x= xy[:,0]*30,
        y= xy[:,1]*30
        )

    source = ColumnDataSource(data = {**xandy,**mydict}
    )
    
    #Creating the tooltips to display the data for the enhanced and the basic types.
    basics =[
        ("index", "$index"),
        ("(x,y)", "($x, $y)"),
    ]
    enhanced = [(datas[i],"@"+datas[i]) for i in range(len(datas))]
    hover = HoverTool(tooltips=basics + enhanced)
    
    #Finaly plot with bokeh
    p = figure(x_range=(-1000,1000), y_range=(-500, 1500),plot_width = 1000,plot_height=1000)
    p.add_tools(hover)
    p.image(image='image',x='x', y='y', dw=32, dh=32,source = source)
    show(p)

#Plot a set of images in polar coordinates with r from the data given in argument and theta from the hue value of the principal color
#rt is a list of  lists
def circle_plot(rt, imagesData,show_notebook=True):
    
    r = rt[0]
    theta = rt[1]
    image = imagesData.extract_lowRes()
    fig = plt.figure(figsize = (170,170))
    ax = plt.subplot(111, projection='polar')
    ax.scatter(theta, r, marker = '.')
    for i in range(len(images)) :
        im = OffsetImage(images[i], cmap = 'gray', zoom=0.75)
        im.image.axis =ax
        ab =AnnotationBbox(im,(theta[i],r[i]),frameon=False) 
        ax.add_artist(ab)
    ax.set_rmax(np.max(r))
    ax.set_rticks([]) 
    ax.grid(True)
    if(not show_notebook):
        filename = easygui.filesavebox(msg = "Give a name to your plot")
        fig.savefig(filename + ".jpg")
        
    else:
        plt.show()
    
#PLot the set of images with its principal color in X and the second one in Y
def two_dimensions_plot(xy,imagesData,show_notebook=True):
    
    x= xy[0]
    y= xy[1]
    images = imagesData.extract_lowRes()
    fig = plt.figure(figsize = (170,170))
    ax = plt.subplot(111)

    ax.scatter(x,y, marker = '.')
    for i in range(len(images)) :
        im = OffsetImage(images[i], cmap = 'gray', zoom=0.5)
        im.image.axis =ax
        ab =AnnotationBbox(im,(x[i],y[i]),frameon=False) 
        ax.add_artist(ab)
        ticks = np.linspace(0,np.max((x,y)),36)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.tick_params(labelsize = 75)
    plt.xlabel('Principal dimension', fontsize=150)
    plt.ylabel('Second principal dimension', fontsize=150)
    if(not show_notebook):
        filename = easygui.filesavebox(msg = "Give a name to your plot")
        fig.savefig(filename + ".jpg")
        
    else:
        plt.show()

def oneD_plot(images,rows,cols):
    size =images[0].shape
    canvas = np.zeros((rows*size[0],cols*size[1],3))
    for i in range(len(images)):
        canvas[int(i/cols)*size[0]:(int(i/cols)+1)*size[0],int(i%cols)*size[1]:(int(i%cols)+1)*size[1]] = images[i] 
    filename = easygui.filesavebox(msg = "Give a name to your plot")
    fig.savefig(filename + ".jpg")    
    
