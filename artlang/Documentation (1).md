
# User documentation


## 1. Module imagedata

### a. ImageData




```python
def add_data(name,value)
```

Adds the data specified in arguments to the dictionary of the current ImageData.

__Parameters__:
> name: (string) the name of the data <br>
> value: (any)   the value of the data


```python
def available_data()
```

Returns the available data for this image

__Returns__: 
> array of the data names


```python
def delete_data(name)
```

Deletes a particular data from the dictionary 

__Parameters__:
> name: (string) the name of the data to delete


```python
def plot_Image()
```

Plot the original image in the notebook using matplotlib


```python
def plot_lowImage()
```

Plot the low resolution image in the notebook using matplotlib

#### Examples:


```python
my_image = imd.ImageData(image) #Create the ImageData
my_image.add_data("hue",0.5)    #Add the value 0.5 to the key hue
my_image.delete("hue")          #Delete the key value pair hue
my_image.plot_Image()           #Plot the original resolution image
```

### b. ImageDataCollection
Support indexing, item assignement and deletion


```python
def from_array(imageArray, data(optional) = [])
```

Class function, must be called on the class. ex: ImageDataCollection.from_array(images)
Returns a ImageDataCollection composed of the images in imageArray, and the associated data dictionary

__Parameters__: 
>imageArray: (arraylike of numpy arrays) the list of images to form the ImageDataCollection <br>
>data: (optional, list of dictionaries) the list of dictionaries to be associted to the images.
    
__Returns__: 
>An ImageDataCollection with the ith image associated with the ith data dictionary


```python
def from_folder()
```

Class function, must be called on the class. ex: ImageDataCollection.from_array() <br>
Returns a ImageDataCollection composed of the images in the selected folder. Opens a dialogbox to select the folder

__Returns__:
>An ImageDaraCollection with the images in the folder, with each images having as data their file path.


```python
def add(imagedata)
```

Adds the given ImageData to the collection

__Parameters__: 
> imagedata: (ImageData) the element to add to the collection

__Raises:__ 
> ValueError: if the argument imagedata is not of type ImageData


```python
def delete(imagedata)
```

Deletes the given ImageData from the collection

__Parameters__: 
> imagedata: (ImageData) the element to delete


```python
def extract_lowRes()
```

Returns all the original resolution images from the collection

__Returns__:
> list of numpy arrays, the images


```python
def extract_highRes()
```

Returns all the low resolution (256x256) images from the collection

__Returns:__
> list of numpy arrays, the low resolution images


```python
def images_with_data(data)
```

Returns the list of images that have this data in their data dictionary

__Parameters__: 
> data: (string) the name of the data to search for

__Returns__ :
> list of ImageData, the elements from the collection having this data


```python
def data_from_csv()
```

Opens a dialog box to select a CSV file. Read this CSV file and fill each ImageData dictionary with the values in the csv

__Raises__:
> ValueError: if the csv contains not the same amount of images than the ImageDataCollection


```python
def save_data_csv()
```

Opens a dialog box to selct the folder where to save the data from each image into a csv file.


```python
def get_data_for_all(name)
```

Returns the list of values for the data name in all the images

__Parameters__: 
> name: (string) the data name
    
__Returns__: 
> a list of values of the images for the data name


```python
def add_data_for_all(name,datas)
```

Adds the list of values from datas to all the images. The ith image will have the ith value.

__Parameters__: 
> name: (string) the data name
> datas:(list) a list of values for the data name 

## 2. Module auto_cropping 


```python
def auto_cropping(imagesData)
```

Returns the cropped images

__Parameters__: 
> imagesData :(ImageDataCollection) the collection to extract the images from
    
__Returns__: 
> a list of numpy arrays, the cropped images


```python
def entropy_list(myimages)
```

Returns the entropiescomputed for each image

__Parameters__: 
> myImages: (arraylike of numpy arrays) the list of images to compute the entropy from
    
__Returns__:
> list of nympy arrays, the entropy images
    

## 3. Module seperate 


```python
def separate_cards_images(imagesData)
```

Separates the images from the photo library cards

__Parameters__: 
> imagesData: (ImageDataCollection) the collection of images where to perform the speraration

__Returns__ :
> toCrop: list of numpy array, the images to crop
> notoCrop:  list of numpy array, the images not to crop

## 4. Module vizualize


```python
def plot_xy(xy,imagesData,show_notebook=True)
```

Plotting function with cartesian coordinates. Mostly used for Hough and Hog coordinates. <br> To plot any two dimensions coordinates, see the two_dimensions_plot function.

__Parameters__: 
> xy: (list of tuples) the x and y coordinates, the ith tuple is associated to the ith image
> imagesData: (ImageDataCollectio) the collection to plot
> show_notebook: (optional) show the plot in the notebook by default, if False opens a dialog box to save the plot in a jpeg 


```python
def bokeh_plot(imagesData,datas,xy)
```

Plotting function using Bokeh, with a hover tool displaying data in the plot.

__Parameters__: 
> xy: (list of tuples) the x and y coordinates, the ith tuple is associated to the ith image <br>
> imagesData: (ImageDataCollectio) the collection to plot <br>
> datas: (list of data name) data to display in the plot with the hover tool


```python
def circle_plot(rt, imagesData,show_notebook=True)
```

Plotting function with polar coordinates

__Parameters__: 
> rt: (list of list) the radius and theta coordinates, the 1st list is the radiuses, the second one the thetas <br>
imagesData: (ImageDataCollectio) the collection to plot <br>
show_notebook: (optional) show the plot in the notebook by default, if False opens a dialog box to save the plot in a jpeg 


```python
def two_dimensions_plot(xy,imagesData,show_notebook=True)
```

PLotting function on two dimensions. 

__Parameters__: 
> xy: (list of list) the x and y coordinates, the 1st list is the x, the second one the y <br>
imagesData: (ImageDataCollectio) the collection to plot <br>
show_notebook: (optional) show the plot in the notebook by default, if False opens a dialog box to save the plot in a jpeg 

## 5. Module tsne_hog


```python
def my_hog(squaredImg)
```

Compute the HOG images for the the list given in arguments

__Parameters__: 
> squaredImg: (list of numpy arrays, ATTENTION: all images must be squared) the images 

__Returns__:
> a list of numpy arrays, the HOG images


```python
def hog_tsne(imagesData)
```

Compute the PCA-TSNE coordinates for the hog tranform. Used to plot similar images close to each others.

__Parameters__: 
> imagesData: (ImageDataCollection) the collection of images to compute from
 
__Returns__:
> list of tuples, the x and y coordinates in the hog embedded space. the first tuple is associated to the first image

## 6. Module hough


```python
def hough_transform(imagesData)
```

Compute the houghn transform for the images in the list given in arguments

__Parameters__: 
> imagesData: (ImageDataCollection) the images 

__Returns__:
> a list of numpy arrays, the hough transforms


```python
def hough_tsne(imagesData)
```

Compute the PCA-TSNE coordinates for the hough tranform. Used to plot similar images close to each others.

__Parameters__: 
> imagesData: (ImageDataCollection) the collection of images to compute from
    
__Returns__:
> list of tuples, the x and y coordinates in the hough embedded space. the first tuple is associated to the first image

## 7. Module sorting


```python
def sortBy(imageData,sortingParam)
```

Sort the collection of images by the given parameter. This parameter can either be hue,sat,val or any data nem present in the data dictionary for all the images. If hue, val or sat is given, the function will compute these values itself. 

__Parameters__:
> imagesData: (ImageDataCollection) the collection of images to sort <br>
sortingParam: (string) the parameter to sort the image with respect to

__Returns__:
> a list of numpy arrays sorted by the parameter

## 8. Module color


```python
def compute_principal_colors(imageData,k)
```

Compute the k principal colors of each image in the collection

__Parameters__: 
> imagesData: (ImageDataCollection) the collection of images to analyse <br> 
k: (integer) the number of principal colors to find

__Returns__:
> list of tuples, the hue value of the k principla color for each images. the ith tuple is associated with the ith image

## 9. Module rijks_api


```python
def searchSome(query,number=100)
```

Search in the Rijksmuseum online archive a given number of images for the search word query

__Parameters__: 
> query: (string) the search word (ex: monet,rembrandt...) <br>
number: (string, optional) the number of images to retrieve
    
__Returns__:
> a csv file with the weblink to images 
    
__Raises__:
> ValueError: if the parameter number is bigger than the number of images available for this query. Will print the maximum number possible for this query


```python
def searchAll(query)
```

Search in the Rijksmuseum online archive all the images for the search word query <br>
ATTENTION: this function can take a lot of time if a lot of images are available

__Parameters__: 
> query: (string) the search word (ex: monet,rembrandt...) <br>
number: (string, optional) the number of images to retrieve
    
__Returns__:
> a csv file with the weblink to images 


```python
def downloadImages(csv)
```

Download all the images from the links in the csv

__Parameters__: 
> csv: (DataFrame) the csv to download from
    
__Returns__:
> integer, the number of images that could not be downloaded


```python
def getDatesFromCSV(csv):
```

Retrieve the publishing dates for the art objects in the csv

__Parameters__: 
> csv: (DataFrame) the csv to analyse
    
__Returns__:
> a dictionary of key value, the key being the id of the image and the value its date 
    


```python

```
