import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from tqdm import tqdm
import skimage.io as io
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.filters import gaussian
import skimage.color as sColor
import skimage.transform as trs
import scipy.optimize


def blur_resize(cards):
    blurredImg = []
    ratios = []
    for img in cards:
        temp = trs.resize(img[30:(img.shape[0]-70),30:(img.shape[1]-30)],(512,512))
        blurredImg.append(gaussian(sColor.rgb2grey(temp),sigma=7))
        ratios.append((512/(img.shape[0]-100),512/(img.shape[1]-60)))
    return blurredImg,ratios
        
def entropy_list(cards):
    entropies = []
    for img in tqdm(blurredImg):
        if np.max(img) >1:
            img = img/np.max(img)
            entropies.append(entropy(img,disk(10)))
    return entropies

def min_max(p,m):
    p = int(round(p))
    return max(0,min(p,m-1))
    

def cropping(x):
    i  =min_max(x[0],image.shape[0])
    j =min_max(x[1],image.shape[1])
    m = min_max(x[2],image.shape[0])
    y = min_max(x[3],image.shape[1])
    tempArea =float((m-i)*(y-j))
    totalArea = float((image.shape[0]*image.shape[1]))
    if(tempArea>0):
        tempMax = ((image[m,y]+image[i,j]-image[m,j] - image[i,y])/tempArea) + l1* tempArea/totalArea
        return -tempMax
    return 0

def optimize(cropzero):
    answer = scipy.optimize.minimize(cropping,cropzero,method = "Nelder-Mead")
    p=[0,0,0,0]
    p[0] = min_max(answer.x[0],512)
    p[1] = min_max(answer.x[1],512)
    p[2] = min_max(answer.x[2],512)
    p[3] = min_max(answer.x[3],512)
    a = (p[3]-p[1])*(p[2]-p[0])
    return p,(-answer.fun),a


def wrapper_function(image) : 
    bestguess = [0,0,0,0]
    bestEnt = 0
    bestArea=0
    tried=[]
    for i  in range(20):
        guess = [0,0,0,0]

        guess[0]= np.random.choice(range(255))
        guess[1]= np.random.choice(range(255))
        guess[2]= np.random.choice(range(256,511))
        guess[3]= np.random.choice(range(256,511))
        tempguess,tempEnt,area = optimize(guess)
        tried.append(tempEnt)
        if(tempEnt>bestEnt):

            init = guess
            bestEnt = tempEnt
            bestguess = tempguess
            bestArea = area
    return bestArea,bestguess,tried

    
def auto_cropping(imagesData):
    #images extraction
    cards= imagesData.extract_highRes()
    
    #blurring and resizing all images to 512x512 and keeping the resizing ratio
    blurredImg,ratios = blur_resize(cards)
    
    #compute the entropy to discard writings and stamps
    entropies=entropy_list(blurredImg)
    
    #compute the integral image, discarding pixels with too high entropy
    integral = []
    for img in entropies:
        integral.append(trs.integral_image(np.clip(img,0,np.percentile(img.flatten(),80))))
    
    #Cropping the black borders (which is extremely common in photolibraries cards
    first_cropped = []
    for img in cards:
        first_cropped.append(img[30:(img.shape[0]-70),30:(img.shape[1]-30)])
    
    #Cropping using the optimizer, respecting the ratio from the images
    final = []
    l1 = 1.8
    for j in range(len(integral)):
        image =integral[j]
        finalArea,finalGuess,finalEnt = algo(image)
        ratioGuess = [0,0,0,0]
        ratioGuess[0] = int(finalGuess[0]/ratios[j][0])
        ratioGuess[1] = int(finalGuess[1]/ratios[j][1])
        ratioGuess[2] = int(finalGuess[2]/ratios[j][0])
        ratioGuess[3] = int(finalGuess[3]/ratios[j][1])
        tresh0 = int(15/ratios[j][0])
        tresh1 = int(15/ratios[j][1])
        im =first_cropped[j][ratioGuess[0]+tresh0:ratioGuess[2]-tresh0,ratioGuess[1]+tresh1:ratioGuess[3]-tresh1]
        if(im.shape[0] <1 or im.shape[1]<1):
            im = bigCropped[j][ratioGuess[0]:ratioGuess[2],ratioGuess[1]:ratioGuess[3]]
        final.append(im)
return final


    
    
    
    
    
    
    
    

    
