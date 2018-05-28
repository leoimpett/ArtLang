import numpy as np
from tqdm import tqdm
import skimage.transform as trs
import skimage.color as color
from skimage.transform import hough_line,hough_line_peaks, probabilistic_hough_line
from sklearn.decomposition import PCA 
from sklearn.manifold import TSNE 

from skimage.feature import canny


def hough_transform(imagesData):
    
    images = imagesData.extract_highres()
    houghImg = []
    images = tqdm(images)
    images.set_description("Computing the hough transforms...")
    for img in images:
        cann = canny(color.rgb2gray(trs.resize(img,(512,512))),low_threshold=0.3,high_threshold=0.7)
        h, theta, d = hough_line(cann)
        fig, axes = plt.subplots(1, 1, figsize=(3, 10))
        plt.imshow(np.log(1 + h),
                 extent=[np.rad2deg(theta[-1]), np.rad2deg(theta[0]), d[-1], d[0]],
                 cmap="gray", aspect=1/1.5)
        plt.axis('off')
        plt.tight_layout(pad=0)
        fig.canvas.draw()
        data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8)
        data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        houghImg.append(data)
        plt.close(fig)
   

    flattened = []
    for elem in houghImg :
        flattened.append(elem.flatten())
        
    hough_pca = PCA(n_components=50).fit_transform(flattened)
    hough_embedded = TSNE(n_components=2).fit_transform(hough_pca)
    
    return hough_embedded
    