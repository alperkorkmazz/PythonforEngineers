import urllib.request

def getAPic(urladdress):
    newPicture="newPicture.jpg"
    urllib.request.urlretrieve(urladdress,newPicture)

a=getAPic("https://upload.wikimedia.org/wikipedia/commons/3/3e/Einstein_1921_by_F_Schmutzer_-_restoration.jpg")
