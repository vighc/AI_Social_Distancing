import urllib.request

print('Yolo3 weight (237MB) is downloading please wait ')

url = 'https://pjreddie.com/media/files/yolov3.weights'
urllib.request.urlretrieve(url, './models/yolov3.weights')

