import numpy as np
import skimage.color as sColor
from skimage.feature import hog
from sklearn.manifold import TSNE 
from sklearn.decomposition import PCA 


def my_hog(squaredImg):
    hogImg = [] 
    for img in squaredImg : 
        tmp, hogIm  =hog(sColor.rgb2grey(img), orientations = 8,pixels_per_cell=(16, 16),
                        cells_per_block=(1, 1),visualise = True, transform_sqrt = True)
        hogImg.append(hogIm)
    return hogImg

def hog_tsne(imagesData):
    images=imagesData.extract_lowRes()
    hogImg = my_hog(images)
    flattened = []
    for img in hogImg :
        flattened.append(img.flatten())
    hog_pca = PCA(n_components=50).fit_transform(flattened)
    hog_embedded = TSNE(n_components=2).fit_transform(hog_pca)
    
    return hog_embedded

        