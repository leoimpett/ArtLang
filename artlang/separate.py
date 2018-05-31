import numpy as np
from tqdm import tqdm
from skimage.feature import hog
from sklearn import svm
import pickle


def separate_cards_images(imagesData):
    file = open("svm.pkl","rb")
    svm = pickle.load(file)
    file.close()
    
    images = imagesData.extract_lowRes()
    high =  imagesData.extract_highRes()
    hogImg = []
    tq = tqdm(images)
    tq.set_description("Computing hogs...")
    for img in tq : 
        tmp, hogIm  =hog(sColor.rgb2grey(img), orientations = 8,pixels_per_cell=(16, 16),
                        cells_per_block=(1, 1),visualise = True, transform_sqrt = True)
        hogImg.append(hogIm.flatten())
    
    prediction = svm.predict(hogImg)
    toCrop =[]
    notToCrop = []
    for i in range(len(images)):
        if(prediction[i]==1.0):
            notToCrop.append(high[i])
        else:
            toCrop.append(high[i])
            
    return toCrop,notToCrop