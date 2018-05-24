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
            imgdata_list.append(ImageData(elem))
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
    
#Adding or saving data to/fromm all images

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
    
    def save_data_csv(self):
        location = easygui.diropenbox(default='/')
        columns = []
        dat = self.images[0].available_data()
        matrix = np.zeros((len(self.images),len(dat)))
        i=0
        for key in dat:
            columns.append(key)
            j=0
            for elem in self.images:
                
                matrix[j,i]=elem.data[key]
                j+=1
            i+=1
        csv = pd.DataFrame(matrix,columns=columns)
        csv.to_csv(location+"/data_Images.csv")
        
#Processing data for all images in the collection 
    def get_data_forall(self,name):
        result  = []
        for elem in self.images:
            x= 0
            try:
                x = elem.data[name]
            except KeyError:
                x=None
            result.append(x)
        return result
    
    def add_data_for_all(self,name,datas):
        if len(data) != len(self.images):
            raise ValueError(
                'Invalid Argument, the array should contain exactly the same number of images as the ImageDataCollection') 
        for i in range(len(self.images)):
                self.images[i].add_data(name,datas[i])