import numpy as np
import pandas as pd
import requests
import wget
import easygui


def searchSome(query,number=100):
    imagesPerPage = 100
    jsonFiles = []
    firstQuery = min(number,imagesPerPage)
    url = requests.get("https://www.rijksmuseum.nl/api/en/collection/?ps="+str(firstQuery)+"&q=Q&key=t2KR0CWi&format=json"
                         .replace("Q", query))
    jsonfile = url.json()
    myCsv = jsonCSV(jsonfile)
    if(number>jsonfile['count']):
        raise ValueError("Illegal Argument: maximum value for param number is " + str(jsonfile['count']))
    if(number>imagesPerPage): 
        number = number - imagesPerPage
        index = 2
        while number > 0 :
            
            url = requests.get("https://www.rijksmuseum.nl/api/en/collection/?p="+str(index)+"&ps=100&q=Q&key=t2KR0CWi&format=json"
                                 .replace("Q", query))
            if(min(number,imagesPerPage)!=imagesPerPage):
                jsonFiles.append(jsonCSV(url.json())[0:number])
            else :
                jsonFiles.append(jsonCSV(url.json()))                

            number = number - imagesPerPage
            index +=1
        for csv in jsonFiles:
            myCsv = pd.concat((myCsv,csv),ignore_index = True)
            
    return myCsv


#Can take a long time for big set of images
def searchAll(query):
    url = requests.get("https://www.rijksmuseum.nl/api/en/collection/?q=Q&key=t2KR0CWi&format=json"
                         .replace("Q", query))
    jsonfile = url.json()
    return searchSome(query,jsonfile['count'])
    
def jsonCSV(file):
    df = pd.DataFrame.from_dict(file['artObjects'])
    return df
def downloadImages(csv):
    directory = easygui.diropenbox(default='/')
    invalid = 0
    for i in range(csv.shape[0]):
        if(csv['webImage'][i] is not None):
            wget.download(csv['webImage'][i]['url'],out=directory+"/RijksmuseumCollection"+str(i)+".jpg")
        else :
            invalid += 1
    return invalid
            
    
def getDatesFromCSV(csv):
    idDate = {}
    ids = csv["id"]
    url = ""
    jsonfile = {}
    for i in range(csv.shape[0]):
        elem = ids[i].upper()[3:]
        if(csv['webImage'][i] is not None):
            r = requests.get("https://www.rijksmuseum.nl/api/nl/collection/"+elem+"?key=t2KR0CWi&format=json")
            jsonfile = r.json()
            idDate[elem] = jsonfile["artObject"]["dating"]['sortingDate']
    return idDate