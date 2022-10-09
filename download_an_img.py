import urllib.request

url = input("Enter image url")             # taking url as input from user
# using urllib liberary
# this function takes two parameter 'url' and name of 'downloaded image'
try:
    urllib.request.urlretrieve(url, 'downloadimage.png')
    print("Image downloaded")
except:
    print("Error")