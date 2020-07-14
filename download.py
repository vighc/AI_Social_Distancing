import urllib
linkToFile = "https://pjreddie.com/media/files/yolov3.weights"
localDestination = "./models/yolov3.weights"
resultFilePath, responseHeaders = urllib.urlretrieve(linkToFile, localDestination)

#%cd ./models/
#!wget https://pjreddie.com/media/files/yolov3.weights
