import urllib.request

print('Beginning file download with urllib2...')

url = 'https://pjreddie.com/media/files/yolov3.weights'
urllib.request.urlretrieve(url, './models/yolov3.weights')

'''import urllib
linkToFile = "https://pjreddie.com/media/files/yolov3.weights"
localDestination = "./models/yolov3.weights"
resultFilePath, responseHeaders = urllib.urlretrieve(linkToFile, localDestination)

#%cd ./models/
#!wget https://pjreddie.com/media/files/yolov3.weights
'''
