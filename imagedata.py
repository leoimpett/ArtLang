import numpy as np
import matplotlib.pyplot as plt
import skimage.transform as trs
import skimage.io as io
import pandas as pd
import easygui

class ImageData :
    def __init__(self,img, dat = {}):
        self.lowImage = trs.resize(img,(256,256))
        self.image = img
        self.data = dict(dat)
    def add_data(self,name,value):
        self.data[name.lower()]=value
    def available_data(self):
        return list(self.data.keys())
    def delete_data(self, name):
        self.data.pop(name)
    def plot_Image(self):
        plt.imshow(self.image)
    def plot_lowImage(self):
        plt.imshow(self.lowImage)
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        if('name' in self.available_data()):
            return self.data['name']          
        else :
            return "UnnamedImage"


class ImageDataCollection : 

# Constructors
    def __init__(self,imagedatas):
        self.images = imagedatas
    @classmethod    
    def from_array(cls,imageArray):
        imgdata_list = []
        for elem in imageArray:
            imagedata = ImageData(elem)
            imgdata_list.append(imagedata)
        return cls(imgdata_list)
    @classmethod
    def from_folder(cls):
        dirname = easygui.diropenbox(default = '/')
        images = io.imread_collection(dirname + '/*.jpg')
        return ImageDataCollection.from_array(images)
    
# Addition, Deletion
    def add(self,imagedata):
        if(type(imagedata) != ImageData):
            raise ValueError('Invalid Argument, imagedata should be of type ImageData')
        self.images.append(imagedata)
    def delete(self,imagedata):
        self.images.remove(imagedata)

# Features from ImageData       
    def extract_lowRes(self):
        result = []
        for elem in self.images:
            result.append(elem.lowImage)
        return result
    def extract_highRes(self):
        result = []
        for elem in self.images:
            result.append(elem.image)
        return result
    def images_with_data(self,data):
        result = []
        for elem in self.images:
            available = elem.available_data()
            if(data in available):
                result.append(elem)
        return result
       
# Indexing, assignement and deletion
    def __getitem__(self,index):
        return self.images[index]
    def __setitem__(self,index,value):
        if(type(value) != ImageData):
            raise ValueError('Invalid Argument, imagedata should be of type ImageData')
        self.images[index] = value
    def __delitem__(self,index):
        return self.images.pop(index)
    
#Adding data from csv

    def data_from_csv(self):
        csvFile = easygui.fileopenbox(filetypes = ['*.csv'])
        data = pd.read_csv(csvFile)
        columns = list(data.columns.values)
        if data.shape[0] != len(self.images):
            raise ValueError(
                'Invalid Argument, the csvFile should contain exactly the same number of images as the ImageDataCollection')
        for col in columns:
            for i in range(len(self.images)):
                self.images[i].add_data(col,data[col][i])
        
    
    