import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import skimage.color as sColor
from datastruct.imagedata import*


def sortBy(imageData,sortingParam) :
    images = imageData.extract_highRes()
    #convert RGB images to HSV images
    paramImages = []
    if(sortingParam == 'hue' or sortingParam == 'val' or sortingParam == 'sat'):
        for image in images :
            hsv = sColor.convert_colorspace(image, 'RGB','HSV')
            if(sortingParam == 'hue') :
                imageHue = hsv[:,:,0]
                val = np.ndarray.flatten(imageHue);
            if(sortingParam == 'sat') :
                imageSat = hsv[:,:,1]
                val = np.ndarray.flatten(imageSat);
            if(sortingParam == 'val') :
                imageVal = hsv[:,:,2]
                val = np.ndarray.flatten(imageVal);
            paramImages.append(val.mean())    
    else:
        if(len(imageData.images_with_data(sortingParam)) != len(images)):
            raise ValueError("The sorting parameter provided is not present for all the images")
        paramImages = list(imageData.get_data_forall(sortingParam))
        
    #Sort the list of images by mean (ascending)
    sorted_indexes = np.argsort(paramImages)
    
    #Select the images from the sorted map and scale them from [0:255] to [0:1]
    rgbImages = []
    for idx in sorted_indexes :
        rgbImages.append(images[idx]/255.0)
        
    return rgbImages;