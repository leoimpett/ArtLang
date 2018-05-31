import numpy as np
from tqdm import tqdm
import skimage.color as sColor
from sklearn.cluster import KMeans


def compute_principal_colors(imageData,k):
    result =[]
    hues = []
    images = imageData.extract_lowRes()
    images = tqdm(images)
    images.set_description("Filtering the images...")
    for img in images :
        hsv = sColor.rgb2hsv(img)
        h = hsv[:,:,0].flatten()
        values = hsv[:,:,2].flatten()
        myzip = zip(h.tolist(),values.tolist())
        filtered = list(filter(lambda x : x[1] !=0,list(myzip)))
        h = np.asarray([x[0] for x in filtered]).flatten()
        h = h.reshape((h.shape[0],1))
        hues.append(h)

    hues= tqdm(hues)
    hues.set_description("Computing the principal colors...")
    for h in tqdm(hues):
        grey = list(filter(lambda x: x!=0,h)) == []
        if(not grey):
            kmeans = KMeans(n_clusters=k).fit(h)
            result.append(kmeans.cluster_centers_)
        else : 
            result.append(np.asarray(np.zeros(k)))
    return result